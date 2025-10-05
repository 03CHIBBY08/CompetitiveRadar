import os
import json
from google import genai
from google.genai import types

# IMPORTANT: KEEP THIS COMMENT - using blueprint:python_gemini
# Note that the newest Gemini model series is "gemini-2.5-flash" or "gemini-2.5-pro"
# do not change this unless explicitly requested by the user
GEMINI_API_KEY = os.environ.get("GEMINI_FREE_API_KEY") or os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def research_agent(competitor_updates):
    """
    Research Agent: Extracts relevant details from competitor updates.
    Takes raw competitor data and structures it with key insights.
    """
    print("🔍 Research Agent: Analyzing competitor updates...")
    
    processed_updates = []
    
    for update in competitor_updates:
        prompt = f"""
        Analyze this competitor update and extract the key details:
        
        Competitor: {update['competitor']}
        Update: {update['update']}
        Date: {update['date']}
        Source: {update['source']}
        
        Extract:
        1. Main feature/change/announcement
        2. Key metrics or numbers mentioned
        3. Target audience or market
        4. Potential business impact
        
        Respond in JSON format with keys: main_point, metrics, target, impact
        """
        
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    types.Content(role="user", parts=[types.Part(text=prompt)])
                ],
                config=types.GenerateContentConfig(
                    system_instruction="You are a business intelligence analyst extracting key insights from competitor updates. Always respond with valid JSON.",
                    response_mime_type="application/json"
                )
            )
            
            content = response.text
            if content:
                analysis = json.loads(content)
            else:
                raise ValueError("Empty response from API")
            
            processed_updates.append({
                "id": update['id'],
                "competitor": update['competitor'],
                "competitor_category": update.get('competitor_category', 'Unknown'),
                "original_update": update.get('update', ''),
                "update": update.get('update', ''),
                "date": update['date'],
                "source": update['source'],
                "source_type": update.get('source_type', 'Unknown'),
                "impact_score": update.get('impact_score', 5),
                "analysis": analysis
            })
            
        except Exception as e:
            print(f"Error processing update {update['id']}: {e}")
            continue
    
    print(f"✅ Research Agent: Processed {len(processed_updates)} updates")
    return processed_updates
