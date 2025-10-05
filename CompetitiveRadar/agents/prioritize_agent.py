import os
import json
from google import genai
from google.genai import types

# IMPORTANT: KEEP THIS COMMENT - using blueprint:python_gemini
# Note that the newest Gemini model series is "gemini-2.5-flash" or "gemini-2.5-pro"
# do not change this unless explicitly requested by the user
GEMINI_API_KEY = os.environ.get("GEMINI_FREE_API_KEY") or os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def prioritize_agent(categorized_updates):
    """
    Prioritization Agent: Scores each update 1-10 based on potential impact for startup founders.
    Considers factors like competitive threat, market impact, and strategic relevance.
    Returns top 3 most important updates.
    """
    print("⚡ Prioritization Agent: Scoring updates by founder impact...")
    
    scored_updates = []
    
    for update in categorized_updates:
        prompt = f"""
        Score this competitor update from 1-10 based on its potential impact on a startup founder's decisions.
        
        Competitor: {update['competitor']}
        Category: {update['category']}
        Update: {update['original_update']}
        Analysis: {json.dumps(update['analysis'])}
        
        Consider:
        - Strategic threat level (does this change the competitive landscape?)
        - Urgency (how quickly should the founder respond?)
        - Impact on roadmap, pricing, or positioning decisions
        - Market signal strength (what does this indicate about market trends?)
        
        Respond in JSON format with keys: 
        - priority_score (1-10, where 10 is highest priority)
        - impact_areas (list of affected areas: roadmap, pricing, positioning, marketing)
        - urgency_level (low, medium, high)
        - strategic_implication (brief explanation)
        """
        
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    types.Content(role="user", parts=[types.Part(text=prompt)])
                ],
                config=types.GenerateContentConfig(
                    system_instruction="You are a strategic advisor for startup founders, evaluating competitive threats and opportunities. Always respond with valid JSON.",
                    response_mime_type="application/json"
                )
            )
            
            content = response.text
            if content:
                priority_data = json.loads(content)
            else:
                raise ValueError("Empty response from API")
            
            scored_updates.append({
                **update,
                "priority_score": priority_data.get('priority_score', 5),
                "impact_areas": priority_data.get('impact_areas', []),
                "urgency_level": priority_data.get('urgency_level', 'medium'),
                "strategic_implication": priority_data.get('strategic_implication', '')
            })
            
        except Exception as e:
            print(f"Error prioritizing update {update['id']}: {e}")
            scored_updates.append({
                **update,
                "priority_score": 5,
                "impact_areas": [],
                "urgency_level": 'medium',
                "strategic_implication": 'Error in prioritization'
            })
    
    # Sort by priority score (highest first) and select top 3
    scored_updates.sort(key=lambda x: x['priority_score'], reverse=True)
    top_updates = scored_updates[:3]
    
    print(f"✅ Prioritization Agent: Selected top 3 from {len(scored_updates)} updates")
    for i, update in enumerate(top_updates, 1):
        print(f"   #{i}: {update['competitor']} - Score: {update['priority_score']}/10")
    
    return top_updates
