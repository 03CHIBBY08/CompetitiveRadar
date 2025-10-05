# CompetitiveRadar - Agentic AI System

## Overview
CompetitiveRadar is an agentic AI application designed for startup founders to transform hours of competitor tracking into a 30-second actionable insight digest. The system uses a multi-agent architecture where four specialized AI agents collaborate to analyze competitor data and generate strategic recommendations.

**Current State**: Fully implemented as a professional web application with modular agent architecture, AI-powered chatbot assistant, and seamless UX. Uses Google Gemini AI (free tier available) with fallback to demo mode.

## Problem Statement
Startup founders waste 3-5 hours per week manually tracking competitors across LinkedIn, websites, and news sources. They get flooded with data but lack clarity on what actually matters for their business decisions.

## Solution Architecture

### Multi-Agent System (4 Specialized Agents)

1. **Research Agent** (`agents/research_agent.py`)
   - Extracts relevant details from competitor updates
   - Identifies features, pricing, marketing campaigns, and key metrics
   - Structures raw data for downstream analysis

2. **Categorization Agent** (`agents/categorize_agent.py`)
   - Classifies updates into Product / Pricing / Marketing categories
   - Provides reasoning and confidence scores for classifications
   - Uses AI-powered semantic understanding

3. **Prioritization Agent** (`agents/prioritize_agent.py`)
   - Scores each update 1-10 based on founder impact
   - Considers competitive threat, urgency, and strategic implications
   - Selects top 3 most important updates for weekly digest

4. **Summarization Agent** (`agents/summarize_agent.py`)
   - Generates beautiful Markdown digest with headlines
   - Creates actionable "Founder Takeaway" with next steps
   - Formats output for presentation and decision-making

## Project Structure

```
CompetitiveRadar/
├── app.py                           # Flask web application (main entry)
├── main.py                          # CLI orchestrator (legacy)
├── demo_data.py                     # Pre-generated demo responses
├── agents/
│   ├── __init__.py
│   ├── research_agent.py           # Agent 1: Research
│   ├── categorize_agent.py         # Agent 2: Categorization
│   ├── prioritize_agent.py         # Agent 3: Prioritization
│   └── summarize_agent.py          # Agent 4: Summarization
├── templates/                       # HTML templates
│   ├── base.html                   # Base template with navigation
│   ├── index.html                  # Home/landing page
│   ├── features.html               # Features page
│   ├── demo.html                   # Live demo page
│   ├── pricing.html                # Pricing tiers page
│   ├── credible.html               # Testimonials/social proof
│   ├── get-started.html            # Sign up page
│   └── digest.html                 # Weekly digest display
├── static/
│   └── css/
│       └── style.css               # Professional styling
├── data/
│   ├── competitor_updates.json     # Original mock data
│   ├── competitor_updates_extended.json  # Extended dataset (10 updates)
│   └── competitor_updates_realtime.json  # Multi-source dataset (20 updates, 50+ sources)
└── weekly_digest.md                # Generated output (created on run)
```

## Technical Stack
- **Language**: Python 3.11
- **Web Framework**: Flask
- **AI Model**: Google Gemini AI (gemini-2.5-flash & gemini-2.5-pro)
- **Architecture**: Modular multi-agent system with AI chatbot
- **Design**: Professional black & white monochrome theme
- **Output**: Web UI with Markdown digest + JSON API + Interactive chatbot

## Usage

### Demo Mode (No API Key Required)
By default, runs in demo mode using pre-generated responses:
```bash
python app.py
```
Visit http://localhost:5000 to view the digest

### Live Mode (Requires Google Gemini API - FREE)
Set environment variables:
```bash
export DEMO_MODE=false
export GEMINI_FREE_API_KEY=your-key-here
python app.py
```
Get your free Gemini API key at: https://aistudio.google.com/apikey

### Web Pages & Endpoints
- `/` - Home page with hero section and value proposition
- `/features` - Detailed features page showing all 4 AI agents
- `/demo` - Interactive demo with live workflow visualization
- `/demo/run` - Execute the demo and generate digest
- `/pricing` - Pricing tiers (Starter, Growth, Enterprise)
- `/credible` - Testimonials and social proof
- `/get-started` - Sign up form for free trial
- `/digest` - View generated weekly digest
- `/api/digest` - Get digest as JSON
- `/api/chat` - AI chatbot endpoint (POST)

### CLI Mode (Legacy)
```bash
python main.py
```

## Business Value

### Key Metrics
- **Time Saved**: 3-5 hours/week → 30 seconds
- **Decision Impact**: Actionable insights for roadmap, pricing, positioning
- **Engagement**: High read rates with clear next steps

### Output Format
The digest includes:
- Top 3 prioritized competitor updates
- Category tags (Product/Pricing/Marketing)
- Strategic "Founder Takeaway" with recommendations
- Engagement simulation (CTR, views, action rates)

## Important Notes

### Google Gemini API (FREE)
- Uses **Google Gemini AI with generous free tier** (15 requests/min)
- Get free API key at: https://aistudio.google.com/apikey
- Store key securely in Replit Secrets as `GEMINI_FREE_API_KEY`
- System uses gemini-2.5-flash for agents, gemini-2.5-pro for summarization
- Falls back to demo mode when API key is unavailable

### Demo Presentation Tips
1. Run the system to generate `weekly_digest.md`
2. Take screenshot of the digest output
3. Show as a "newsletter" founders could subscribe to
4. Highlight the multi-agent collaboration in console output
5. Emphasize business outcomes (time saved, actionable insights)

## Recent Changes
- **October 5, 2025 (Night)**: Strategic Emoji Enhancement for Better UX
  - **Strategically Added Emojis** - Enhanced visual appeal and user engagement with thoughtfully placed emojis:
    - **Hero Section**: 🧭 compass emoji in main heading for navigation/guidance theme
    - **Agent Cards**: 🔍 Research, 🏷️ Categorization, ⚡ Prioritization, 📝 Summarization agents
    - **Feature Lists**: ✓ checkmarks for better scannability (pricing tiers, agent features)
    - **Demo Page Sources**: 📱 Social Media, 🚀 Product Launch, 📰 Press, 💼 Company Sites, 📊 App Stores, 🎯 Marketing, 🎙️ Podcasts, 📧 Email
    - **Stat Boxes (Features Page)**: ⏰ Time Saved, 🎯 Actionable Insights
    - **Use Cases (Credible Page)**: 🎯 Roadmap, 💰 Pricing, 📢 Marketing, 💼 Sales
    - **Benefits (Get Started)**: ✅ Setup, 🤖 AI Agents, 📊 Digests, 💡 Recommendations, 🔄 Flexibility
    - **Trust Text**: 🔒 Security, ⚡ Uptime, 💬 Support (get-started page footer)
    - **Chatbot**: 💬 toggle, 🤖 header, 👋 greeting, ➤ send button, ✕ close
    - **CTAs**: ▶️ See Demo, ✨ Start Free Trial, 🚀 Explore/Get Started, 🔄 Run Again, 📄 Print, 📥 Export, 💼 Contact Sales
    - **Demo Actions**: ✅ Success messages, 🔍 Multi-Source title  
    - **Onboarding**: ✨ Generating header, 🎉 Success celebration
    - **Footer**: 🤖 AI Agents Connected badge
  - **Global Loading Animation System** - Enhanced UX with loading feedback:
    - Full-screen loading overlay with spinner for page navigation
    - Button-level loading indicators with spinning animation
    - Smart detection to avoid interfering with chatbot interactions
    - Smooth transitions and professional animations throughout
  - **Design Philosophy**: Emojis used strategically for visual hierarchy, engagement, and better scannability without overwhelming the professional aesthetic

- **October 5, 2025 (Late Evening)**: AI-Powered Onboarding Flow
  - **5-Step Guided Onboarding** - Complete user flow from signup to personalized digest:
    1. **Startup Type Selection** - Choose from 10 industry categories (SaaS, E-commerce, FinTech, etc.)
    2. **Description Input** - Describe your startup with helpful tips and validation
    3. **AI Competitor Discovery** - Gemini AI analyzes description and discovers 10-12 real competitors
    4. **Top 3 Selection** - Interactive selection with category badges and competitor details
    5. **Personalized Digest** - Automated generation with progress animation and completion
  - **Real Data Fetching** - No more static demo data; AI discovers actual competitors based on user input
  - **Intelligent Categorization** - Each competitor labeled as Direct Competitor, Market Leader, Emerging Threat, or Adjacent Player
  - **Session Management** - State persisted across onboarding steps with Flask sessions
  - **Gemini AI Integration** - Uses Google Gemini API for competitor discovery with JSON schema validation
  - **Graceful Fallbacks** - Demo mode with curated competitors when API unavailable
  - **Professional UX** - Progress indicators, loading animations, smooth transitions, visual feedback
  - **Routes Added**: `/onboarding/startup-type`, `/onboarding/description`, `/onboarding/discovery`, `/onboarding/select-top`, `/onboarding/complete`, `/onboarding/generating`, `/onboarding/personalized-digest`
  - **API Endpoints**: `/api/competitors/discover`, `/api/generate-personalized-digest`

- **October 5, 2025 (Evening)**: Multi-Source Scanning & Competitor Categorization
  - **50+ Source Integration** - Real competitive intelligence from diverse channels:
    - Social Media: LinkedIn, Twitter/X, TikTok
    - Product Launch: Product Hunt, Hacker News
    - Press & Media: TechCrunch, VentureBeat, Podcasts
    - Marketing: Email campaigns, Marketing funnels
    - Other: Company websites, App stores, YouTube
  - **Competitor Categorization for Startup Founders**:
    - Direct Competitor (your immediate rivals)
    - Market Leader (established players to monitor)
    - Emerging Threat (fast-growing startups)
    - Adjacent Player (related but different market)
  - **Enhanced Digest Display**:
    - Shows competitor category for each insight
    - Displays source attribution (e.g., "TechCrunch (Press Release)")
    - Impact scores (1-10) and urgency levels (high/medium/low)
    - Multi-source scan badge in digest title
  - **Demo Visualization**:
    - Added "Multi-Source Competitor Scanning" section
    - Visual grid showing all 8 source categories
    - Agent workflow updated to highlight categorization step

- **October 5, 2025 (PM)**: Enhanced UI/UX and AI Chatbot Integration
  - **Converted to Google Gemini AI** - Switched from OpenAI to free Gemini API
  - **AI Chatbot Widget** - Floating chatbot in bottom-right corner for user guidance
    - AI-powered responses using Gemini (with rule-based fallback)
    - Quick suggestion buttons for common questions
    - Typing indicators and smooth animations
    - Robust error handling with graceful degradation
  - **Enhanced UI/UX**
    - Professional black & white monochrome design theme
    - Smooth animations: fadeIn, slideUp, hover effects on all cards
    - Loading spinners and transition effects
    - Improved responsive design for mobile
  - **Security & Reliability**
    - Hardened error handling in chatbot (frontend & backend)
    - Input sanitization with HTML escaping
    - Graceful API failure handling
  
- **October 5, 2025 (AM)**: Multi-page web application complete
  - Built 7 professional pages (Home, Features, Demo, Pricing, Credible, Get Started, Digest)
  - Implemented responsive navigation with active page highlighting
  - Added live demo workflow visualization showing all 4 agents in action
  - Created comprehensive CSS styling matching modern SaaS design
  - Expanded competitor dataset with 10 realistic updates
  - All routes tested and working without errors
  - Ready for deployment on Autoscale

## Future Enhancements
- Real-time competitor data integration (web scraping, APIs)
- Persistent storage for historical trend analysis
- Slack/Notion integration for automated delivery
- Personalized prioritization based on founder preferences
- Interactive web dashboard for digest visualization
