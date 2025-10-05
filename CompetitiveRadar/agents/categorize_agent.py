import os
import json
from google import genai
from google.genai import types

# IMPORTANT: KEEP THIS COMMENT - using blueprint:python_gemini
# Note that the newest Gemini model series is "gemini-2.5-flash" or "gemini-2.5-pro"
# do not change this unless explicitly requested by the user
GEMINI_API_KEY = os.environ.get("GEMINI_FREE_API_KEY") or os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def categorize_agent(processed_updates):
    """
    Categorization Agent: Classifies each update into Product / Pricing / Marketing.
    Uses AI to determine the primary category based on content analysis.
    """
    print("🏷️  Categorization Agent: Classifying updates...")
    
    categorized_updates = []
    
    for update in processed_updates:
        prompt = f"""
        Classify this competitor update into ONE primary category:
        
        Competitor: {update['competitor']}
        Update: {update['original_update']}
        Analysis: {json.dumps(update['analysis'])}
        
        Categories:
        - Product: New features, product launches, technical updates, integrations
        - Pricing: Pricing changes, new pricing tiers, discounts, pricing strategy
        - Marketing: Campaigns, branding, content marketing, partnerships, PR
        
        Respond in JSON format with keys: category, reasoning, confidence (0-1)
        """
        
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    types.Content(role="user", parts=[types.Part(text=prompt)])
                ],
                config=types.GenerateContentConfig(
                    system_instruction="You are a business strategist categorizing competitive intelligence. Always respond with valid JSON.",
                    response_mime_type="application/json"
                )
            )
            
            content = response.text
            if content:
                categorization = json.loads(content)
            else:
                raise ValueError("Empty response from API")
            
            # If category already exists in data, use it; otherwise use AI categorization
            existing_category = update.get('category')
            if existing_category:
                categorized_updates.append({
                    **update,
                    "category": existing_category,
                    "category_reasoning": categorization.get('reasoning', ''),
                    "category_confidence": categorization.get('confidence', 0.8)
                })
            else:
                categorized_updates.append({
                    **update,
                    "category": categorization['category'],
                    "category_reasoning": categorization.get('reasoning', ''),
                    "category_confidence": categorization.get('confidence', 0.8)
                })
            
        except Exception as e:
            print(f"Error categorizing update {update['id']}: {e}")
            categorized_updates.append({
                **update,
                "category": "Unknown",
                "category_reasoning": "Error in categorization",
                "category_confidence": 0.0
            })
    
    print(f"✅ Categorization Agent: Classified {len(categorized_updates)} updates")
    return categorized_updates
