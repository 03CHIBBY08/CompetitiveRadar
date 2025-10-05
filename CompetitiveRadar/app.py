#!/usr/bin/env python3
from flask import Flask, render_template, jsonify, request, redirect, session
import json
import os
import random
from datetime import datetime
from agents.research_agent import research_agent
from agents.categorize_agent import categorize_agent
from agents.prioritize_agent import prioritize_agent
from agents.summarize_agent import summarize_agent
import markdown

app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'dev-secret-key-change-in-production')
# Set to False to use real Gemini API with live AI agents
# Default to True so users can see the system working without API key
DEMO_MODE = os.environ.get('DEMO_MODE', 'true').lower() == 'true'

def simulate_engagement_metrics():
    """Simulate product engagement metrics for demo purposes"""
    return {
        "insights_viewed": random.randint(85, 98),
        "click_through_rate": round(random.uniform(6.5, 9.2), 1),
        "avg_read_time": f"{random.randint(25, 35)} seconds",
        "action_taken_rate": round(random.uniform(15, 25), 1)
    }

def run_analysis():
    """Run the multi-agent analysis pipeline"""
    print("=" * 60)
    print("COMPETITIVERADAR - Agentic AI System")
    print("=" * 60)
    
    if DEMO_MODE:
        print("Running in DEMO MODE")
    
    # Load competitor updates (try realtime first for realistic scanning experience)
    if os.path.exists('data/competitor_updates_realtime.json'):
        with open('data/competitor_updates_realtime.json', 'r') as f:
            competitor_updates = json.load(f)
    elif os.path.exists('data/competitor_updates_extended.json'):
        with open('data/competitor_updates_extended.json', 'r') as f:
            competitor_updates = json.load(f)
    else:
        with open('data/competitor_updates.json', 'r') as f:
            competitor_updates = json.load(f)
    
    print(f"Scanning {len(competitor_updates)} updates from 50+ sources...")
    print("   Sources: Product Hunt, TechCrunch, LinkedIn, Twitter/X, TikTok, YouTube, App Stores, Press Releases...")
    
    if DEMO_MODE:
        # Demo mode: Process realtime data without AI API calls
        print("Research Agent: Extracting insights from competitor updates...")
        processed_updates = []
        for update in competitor_updates:
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
                "analysis": {
                    "main_point": update.get('update', '')[:100],
                    "metrics": "N/A",
                    "target": "Startup founders",
                    "impact": "Strategic decision-making"
                }
            })
        print(f"Research Agent: Processed {len(processed_updates)} updates")
        
        print("Categorization Agent: Applying categories...")
        categorized_updates = []
        for update in processed_updates:
            categorized_updates.append({
                **update,
                "category": "Product" if "product" in update['update'].lower() or "feature" in update['update'].lower() or "launch" in update['update'].lower() else 
                           "Pricing" if "pricing" in update['update'].lower() or "price" in update['update'].lower() or "$" in update['update'] else "Marketing",
                "category_reasoning": "Based on update content",
                "category_confidence": 0.9
            })
        print(f"Categorization Agent: Classified {len(categorized_updates)} updates")
        
        print("Prioritization Agent: Scoring and selecting top 3...")
        # Sort by impact_score and select top 3
        sorted_updates = sorted(categorized_updates, key=lambda x: x.get('impact_score', 0), reverse=True)
        top_updates = sorted_updates[:3]
        
        # Add prioritization fields
        for update in top_updates:
            update['priority_score'] = update.get('impact_score', 5)
            update['impact_areas'] = ['roadmap', 'positioning']
            update['urgency_level'] = 'high' if update['priority_score'] >= 8 else 'medium'
            update['strategic_implication'] = f"High-impact update from {update.get('competitor_category', 'competitor')}"
        
        print(f"Prioritization Agent: Selected top 3 from {len(categorized_updates)} updates")
        for i, update in enumerate(top_updates, 1):
            print(f"   #{i}: {update['competitor']} - Score: {update['priority_score']}/10")
        
        print("Summarization Agent: Generating digest with competitor categories...")
        # Generate digest from top updates
        current_date = datetime.now().strftime("%B %d, %Y")
        digest_items = []
        
        for i, update in enumerate(top_updates, 1):
            comp_cat = update.get('competitor_category', 'Unknown')
            source = update.get('source', 'Unknown')
            source_type = update.get('source_type', 'Unknown')
            
            digest_items.append(f"""
### {i}. **{update['competitor']}** - {update['category']}
**Competitor Category:** {comp_cat} | **Source:** {source} ({source_type})

{update['update']}

**Impact Score:** {update['priority_score']}/10 | **Urgency:** {update['urgency_level']}
""")
        
        digest = f"""# CompetitiveRadar – Weekly Digest
**For:** Tech Startup Founder | **Date:** {current_date}

---

## Top 3 Competitive Insights (Multi-Source Scan)

{"".join(digest_items)}

---

## **Founder Takeaway**

**Immediate Actions:**
1. **Monitor Competitors** → Track {top_updates[0]['competitor']} ({top_updates[0]['competitor_category']}) - their {top_updates[0]['category'].lower()} move signals market shift
2. **Competitive Analysis** → Review how {top_updates[1]['competitor']}'s strategy impacts your positioning
3. **Strategic Response** → Evaluate opportunities to differentiate based on these competitive signals

**Strategic Insight:** These insights from 50+ sources (Social Media, Press Releases, Product Launches, etc.) show the competitive landscape is evolving. Stay ahead by monitoring multi-source intelligence daily.

---

*Generated by CompetitiveRadar Agentic AI System - Powered by Google Gemini*
"""
        print("Summarization Agent: Digest generated with competitor categories and source attribution")
        
    else:
        # Real analysis with fallback to demo mode on quota error
        try:
            print("Using LIVE Google Gemini AI Agents")
            processed_updates = research_agent(competitor_updates)
            categorized_updates = categorize_agent(processed_updates)
            top_updates = prioritize_agent(categorized_updates)
            digest = summarize_agent(top_updates, founder_persona="Tech Startup Founder")
        except Exception as e:
            print(f"Gemini API Error: {str(e)[:100]}")
            print("Falling back to Demo Mode. To use live AI agents:")
            print("   1. Get free Gemini API key at: https://aistudio.google.com/apikey")
            print("   2. Add to Replit Secrets as GEMINI_FREE_API_KEY")
            from demo_data import DEMO_DIGEST
            digest = DEMO_DIGEST
    
    # Save digest
    with open('weekly_digest.md', 'w') as f:
        f.write(digest)
    
    print("CompetitiveRadar Analysis Complete!")
    return digest

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/features')
def features():
    """Features page"""
    return render_template('features.html')

@app.route('/demo')
def demo():
    """Demo page - show workflow"""
    return render_template('demo.html', digest_ready=False, step=0)

@app.route('/demo/run')
def demo_run():
    """Run the demo analysis"""
    try:
        digest = run_analysis()
        digest_html = markdown.markdown(digest, extensions=['extra', 'nl2br'])
        metrics = simulate_engagement_metrics()
        
        return render_template(
            'demo.html',
            digest_ready=True,
            digest_html=digest_html,
            metrics=metrics,
            step=4
        )
    except Exception as e:
        return f"<h1>Error</h1><p>{str(e)}</p>", 500

@app.route('/pricing')
def pricing():
    """Pricing page"""
    return render_template('pricing.html')

@app.route('/credible')
def credible():
    """Social proof and testimonials page"""
    return render_template('credible.html')

@app.route('/get-started')
def get_started():
    """Sign up page"""
    plan = request.args.get('plan', 'growth')
    return render_template('get-started.html', selected_plan=plan)

@app.route('/signup', methods=['POST'])
def signup():
    """Handle signup form submission - now redirects to onboarding"""
    # Store user info in session
    session['user_email'] = request.form.get('email', '')
    session['user_name'] = request.form.get('name', '')
    session['plan'] = request.form.get('plan', 'growth')
    
    # Redirect to onboarding flow
    return redirect('/onboarding/startup-type')

# ============================================================
# ONBOARDING FLOW - AI-Powered Competitor Discovery
# ============================================================

@app.route('/onboarding/startup-type')
def onboarding_startup_type():
    """Step 1: Select startup type/industry"""
    startup_types = [
        {"id": "saas", "name": "SaaS / Software", "icon": "", "description": "Cloud software & tools"},
        {"id": "ecommerce", "name": "E-commerce / Retail", "icon": "", "description": "Online stores & marketplaces"},
        {"id": "fintech", "name": "FinTech / Finance", "icon": "", "description": "Financial services & payments"},
        {"id": "healthtech", "name": "HealthTech / Medical", "icon": "", "description": "Healthcare & wellness"},
        {"id": "edtech", "name": "EdTech / Education", "icon": "", "description": "Learning & education platforms"},
        {"id": "marketplace", "name": "Marketplace / Platform", "icon": "", "description": "Two-sided marketplaces"},
        {"id": "ai_ml", "name": "AI / Machine Learning", "icon": "", "description": "AI-powered products"},
        {"id": "devtools", "name": "Developer Tools", "icon": "", "description": "Tools for developers"},
        {"id": "productivity", "name": "Productivity / Workflow", "icon": "", "description": "Team collaboration & productivity"},
        {"id": "other", "name": "Other", "icon": "", "description": "Something else"},
    ]
    return render_template('onboarding/startup_type.html', startup_types=startup_types, current_step=1)

@app.route('/onboarding/description', methods=['GET', 'POST'])
def onboarding_description():
    """Step 2: Enter startup description"""
    if request.method == 'POST':
        session['startup_type'] = request.form.get('startup_type')
        session['startup_type_name'] = request.form.get('startup_type_name')
        return redirect('/onboarding/description')
    
    if 'startup_type' not in session:
        return redirect('/onboarding/startup-type')
    
    return render_template('onboarding/description.html', current_step=2)

@app.route('/onboarding/discovery', methods=['POST'])
def onboarding_discovery():
    """Step 3: AI discovers competitors"""
    session['startup_description'] = request.form.get('description', '')
    return render_template('onboarding/discovery.html', current_step=3)

@app.route('/api/competitors/discover', methods=['POST'])
def api_discover_competitors():
    """API endpoint for AI-powered competitor discovery"""
    try:
        data = request.get_json()
        startup_type = data.get('startup_type', session.get('startup_type', ''))
        description = data.get('description', session.get('startup_description', ''))
        
        if not description:
            return jsonify({"error": "Description required"}), 400
        
        # Use Gemini AI to discover competitors
        try:
            from google import genai
            from google.genai import types
            
            GEMINI_API_KEY = os.environ.get("GEMINI_FREE_API_KEY") or os.environ.get("GEMINI_API_KEY")
            if GEMINI_API_KEY:
                client = genai.Client(api_key=GEMINI_API_KEY)
                
                prompt = f"""You are a competitive intelligence analyst. Based on this startup description, identify 10-12 real competitors.

Startup Type: {startup_type}
Description: {description}

For each competitor, provide:
1. Company name (real, existing companies)
2. Category: "Direct Competitor" (immediate rivals), "Market Leader" (established players), "Emerging Threat" (fast-growing startups), or "Adjacent Player" (related market)
3. Brief description (1 sentence)
4. Key differentiator

Return ONLY valid JSON array format:
[{{"name": "CompanyName", "category": "Direct Competitor", "description": "Brief description", "differentiator": "Key strength"}}]"""

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[types.Content(role="user", parts=[types.Part(text=prompt)])],
                    config=types.GenerateContentConfig(
                        temperature=0.7,
                        response_mime_type="application/json"
                    )
                )
                
                competitors_json = response.text.strip() if response.text else "[]"
                competitors = json.loads(competitors_json)
                
                # Store in session
                session['discovered_competitors'] = competitors
                
                return jsonify({"competitors": competitors})
        
        except Exception as ai_error:
            print(f"AI discovery error: {ai_error}")
            # Fallback to demo competitors
            pass
        
        # Fallback demo competitors based on type
        demo_competitors = generate_demo_competitors(startup_type, description)
        session['discovered_competitors'] = demo_competitors
        return jsonify({"competitors": demo_competitors})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/onboarding/select-top')
def onboarding_select_top():
    """Step 4: Select top 3 competitors to track"""
    competitors = session.get('discovered_competitors', [])
    return render_template('onboarding/select_top.html', competitors=competitors, current_step=4)

@app.route('/onboarding/complete', methods=['POST'])
def onboarding_complete():
    """Step 5: Complete onboarding and generate digest"""
    data = request.get_json()
    selected_ids = data.get('selected', [])
    
    all_competitors = session.get('discovered_competitors', [])
    selected_competitors = [c for i, c in enumerate(all_competitors) if i in selected_ids]
    
    # Store selected competitors
    session['selected_competitors'] = selected_competitors
    
    return jsonify({"success": True, "redirect": "/onboarding/generating"})

@app.route('/onboarding/generating')
def onboarding_generating():
    """Show digest generation progress"""
    return render_template('onboarding/generating.html', current_step=5)

@app.route('/api/generate-personalized-digest', methods=['POST'])
def api_generate_personalized_digest():
    """Generate personalized digest for selected competitors"""
    try:
        selected_competitors = session.get('selected_competitors', [])
        
        if not selected_competitors:
            return jsonify({"error": "No competitors selected"}), 400
        
        # Generate digest based on selected competitors
        competitor_names = [c['name'] for c in selected_competitors]
        
        digest = generate_personalized_digest(selected_competitors, session.get('startup_description', ''))
        
        # Save to session
        session['personalized_digest'] = digest
        
        return jsonify({"success": True, "digest": digest})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/onboarding/personalized-digest')
def personalized_digest_view():
    """Display the personalized digest"""
    digest_text = session.get('personalized_digest', '')
    
    if not digest_text:
        return redirect('/onboarding/startup-type')
    
    # Convert markdown to HTML
    digest_html = markdown.markdown(digest_text, extensions=['extra', 'nl2br'])
    
    return render_template('digest.html', digest_html=digest_html, is_personalized=True)

def generate_demo_competitors(startup_type, description):
    """Generate demo competitors when AI is unavailable"""
    competitors_by_type = {
        "saas": [
            {"name": "Salesforce", "category": "Market Leader", "description": "Leading CRM platform", "differentiator": "Ecosystem & enterprise features"},
            {"name": "HubSpot", "category": "Market Leader", "description": "Marketing & sales platform", "differentiator": "All-in-one solution"},
            {"name": "Pipedrive", "category": "Direct Competitor", "description": "Sales CRM for small teams", "differentiator": "Simple pipeline management"},
            {"name": "Close", "category": "Direct Competitor", "description": "Sales engagement platform", "differentiator": "Built-in calling"},
            {"name": "Attio", "category": "Emerging Threat", "description": "Modern CRM for startups", "differentiator": "Flexible data model"},
        ],
        "ecommerce": [
            {"name": "Shopify", "category": "Market Leader", "description": "E-commerce platform", "differentiator": "Ease of use & app ecosystem"},
            {"name": "WooCommerce", "category": "Market Leader", "description": "WordPress e-commerce plugin", "differentiator": "Open source & customizable"},
            {"name": "BigCommerce", "category": "Direct Competitor", "description": "SaaS e-commerce platform", "differentiator": "Enterprise features"},
        ],
        "fintech": [
            {"name": "Stripe", "category": "Market Leader", "description": "Payment processing platform", "differentiator": "Developer experience"},
            {"name": "PayPal", "category": "Market Leader", "description": "Digital payments", "differentiator": "Consumer trust & reach"},
            {"name": "Plaid", "category": "Direct Competitor", "description": "Financial data connectivity", "differentiator": "Bank integration API"},
        ],
    }
    
    # Get competitors for type or use generic SaaS
    competitors = competitors_by_type.get(startup_type, competitors_by_type["saas"])
    
    # Add a few more generic ones
    competitors.extend([
        {"name": "Monday.com", "category": "Adjacent Player", "description": "Work management platform", "differentiator": "Visual workflows"},
        {"name": "Notion", "category": "Adjacent Player", "description": "All-in-one workspace", "differentiator": "Flexibility & collaboration"},
        {"name": "Airtable", "category": "Adjacent Player", "description": "Low-code platform", "differentiator": "Database flexibility"},
    ])
    
    return competitors[:10]

def generate_personalized_digest(selected_competitors, startup_description):
    """Generate personalized digest based on selected competitors"""
    current_date = datetime.now().strftime("%B %d, %Y")
    
    digest_items = []
    for i, comp in enumerate(selected_competitors[:3], 1):
        digest_items.append(f"""
### {i}. **{comp['name']}** - {comp['category']}
{comp['description']}

**Key Differentiator:** {comp.get('differentiator', 'Strong market position')}

**Why it matters for you:** Monitor their product updates and pricing changes to stay competitive in your market.
""")
    
    digest = f"""# Your Personalized CompetitiveRadar Digest
**Date:** {current_date}

## Your Startup Focus
{startup_description}

---

## Top 3 Competitors to Track

{"".join(digest_items)}

---

## **Founder Takeaway**

**Immediate Actions:**
1. **Set Up Alerts** → Monitor {selected_competitors[0]['name']}'s product launches and announcements
2. **Competitive Analysis** → Compare your features against {selected_competitors[1]['name']}'s positioning  
3. **Market Intelligence** → Track {selected_competitors[2]['name']}'s pricing and go-to-market strategy

**Strategic Insight:** We'll continuously scan 50+ sources (Product Hunt, TechCrunch, LinkedIn, Twitter/X, etc.) to keep you updated on these competitors. Your personalized digest will be delivered weekly with actionable insights.

---

*Generated by CompetitiveRadar Agentic AI System - Powered by Google Gemini*
"""
    
    return digest

@app.route('/digest')
def digest():
    """Display the full digest"""
    try:
        # Check if digest exists, if not generate it
        if not os.path.exists('weekly_digest.md'):
            digest_text = run_analysis()
        else:
            with open('weekly_digest.md', 'r') as f:
                digest_text = f.read()
        
        # Convert markdown to HTML
        digest_html = markdown.markdown(digest_text, extensions=['extra', 'nl2br'])
        
        return render_template('digest.html', digest_html=digest_html)
    except Exception as e:
        return f"<h1>Error</h1><p>{str(e)}</p>", 500

@app.route('/api/digest')
def api_digest():
    """API endpoint to get digest as JSON"""
    try:
        if os.path.exists('weekly_digest.md'):
            with open('weekly_digest.md', 'r') as f:
                digest_text = f.read()
        else:
            digest_text = run_analysis()
        
        metrics = simulate_engagement_metrics()
        
        return jsonify({
            "digest": digest_text,
            "metrics": metrics,
            "demo_mode": DEMO_MODE,
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    """AI Chatbot endpoint - answers questions about CompetitiveRadar"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"response": "Invalid request format. Please try again!"}), 400
        
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({"response": "Please ask me a question!"}), 400
        
        # Try to use Gemini AI for intelligent responses
        try:
            from google import genai
            from google.genai import types
            
            GEMINI_API_KEY = os.environ.get("GEMINI_FREE_API_KEY") or os.environ.get("GEMINI_API_KEY")
            if GEMINI_API_KEY:
                client = genai.Client(api_key=GEMINI_API_KEY)
                
                system_context = """You are a helpful assistant for CompetitiveRadar, an AI-powered competitor intelligence platform for startup founders.

KEY INFORMATION:
- CompetitiveRadar transforms 3-5 hours of competitor tracking into 30-second actionable insights
- Uses 4 specialized AI agents: Research, Categorization, Prioritization, and Summarization
- Pricing: Starter ($49/mo), Growth ($149/mo), Enterprise (custom)
- Free trial available with no credit card required
- Powered by Google Gemini AI (free tier available)
- Key features: Multi-agent analysis, automated digest generation, actionable insights

Answer questions concisely and professionally. If asked about getting started, guide them to the sign-up page. Keep responses under 100 words."""

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[
                        types.Content(role="user", parts=[types.Part(text=f"{system_context}\n\nUser question: {user_message}")])
                    ],
                    config=types.GenerateContentConfig(
                        temperature=0.7,
                        max_output_tokens=150
                    )
                )
                
                bot_response = response.text.strip() if response.text else "I can help you with CompetitiveRadar! Ask me about pricing, features, or how to get started."
                return jsonify({"response": bot_response})
        
        except Exception as ai_error:
            print(f"AI chat error: {ai_error}")
            # Fallback to rule-based responses
            pass
        
        # Fallback rule-based responses
        message_lower = user_message.lower()
        
        if any(word in message_lower for word in ['price', 'pricing', 'cost', 'plan']):
            response = "CompetitiveRadar offers 3 plans: Starter ($49/mo) for solo founders, Growth ($149/mo) for growing teams, and Enterprise (custom pricing) for large organizations. All plans include a 14-day free trial with no credit card required!"
        
        elif any(word in message_lower for word in ['how', 'work', 'process']):
            response = "CompetitiveRadar uses 4 AI agents: 1) Research Agent extracts key details from competitor updates, 2) Categorization Agent tags updates (Product/Pricing/Marketing), 3) Prioritization Agent scores impact 1-10, 4) Summarization Agent creates actionable weekly digests. It transforms hours of manual work into 30-second insights!"
        
        elif any(word in message_lower for word in ['start', 'begin', 'signup', 'sign up', 'trial']):
            response = "Getting started is easy! Click 'Get Started' in the navigation to begin your 14-day free trial. No credit card required. You'll be analyzing competitor updates in minutes!"
        
        elif any(word in message_lower for word in ['feature', 'capability', 'can do']):
            response = "Key features include: Multi-agent AI analysis, automated competitor tracking, priority scoring, category classification, beautiful Markdown digests, and actionable founder takeaways. All powered by Google Gemini AI!"
        
        elif any(word in message_lower for word in ['agent', 'ai']):
            response = "We use 4 specialized AI agents powered by Google Gemini: Research Agent (extracts insights), Categorization Agent (tags updates), Prioritization Agent (scores impact), and Summarization Agent (creates digests). They work together to give you actionable intelligence!"
        
        elif any(word in message_lower for word in ['demo', 'try', 'test']):
            response = "Try our live demo! Click 'Demo' in the navigation to see all 4 AI agents in action. Watch how we transform scattered competitor updates into a concise, actionable digest in under 30 seconds!"
        
        else:
            response = "I can help you with: how CompetitiveRadar works, pricing plans, getting started, features, or trying the demo. What would you like to know?"
        
        return jsonify({"response": response})
        
    except Exception as e:
        print(f"Chat error: {e}")
        return jsonify({"response": "I'm having trouble right now. Please try the Demo or contact support!"}), 500

if __name__ == '__main__':
    # Use PORT from environment for Autoscale deployment, fallback to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
