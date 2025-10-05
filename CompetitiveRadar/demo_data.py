"""
Demo data for CompetitiveRadar - pre-generated responses for demo mode
"""

DEMO_PROCESSED_UPDATES = [
    {
        "id": 1,
        "competitor": "Competitor A (NotionAI)",
        "original_update": "Launched AI-powered dashboard analytics feature that automatically generates insights from workspace data. The feature uses machine learning to identify productivity patterns and suggest workflow optimizations. Early beta users report 40% increase in team efficiency.",
        "date": "2025-10-01",
        "source": "Product Hunt launch",
        "analysis": {
            "main_point": "AI-powered dashboard analytics with ML-driven productivity insights",
            "metrics": "40% efficiency increase among beta users",
            "target": "Teams seeking workflow optimization and productivity gains",
            "impact": "Sets new standard for AI-native productivity tools, pressures competitors to add similar features"
        }
    },
    {
        "id": 2,
        "competitor": "Competitor B (ClickUp)",
        "original_update": "Increased enterprise pricing tier from $19/user to $25/user (31% increase). New pricing includes advanced automation features and priority support. Grandfathering existing customers for 6 months.",
        "date": "2025-09-28",
        "source": "Pricing page update",
        "analysis": {
            "main_point": "31% enterprise pricing increase with enhanced feature bundle",
            "metrics": "$19 to $25/user, 6-month grandfather period",
            "target": "Enterprise customers, signals premium positioning",
            "impact": "Creates pricing gap opportunity for mid-tier competitors, validates premium automation value"
        }
    },
    {
        "id": 6,
        "competitor": "Competitor F (Airtable)",
        "original_update": "Partnered with Salesforce for native CRM integration. Integration allows bi-directional data sync and automated workflow triggers. Partnership announced at major industry conference with significant media coverage.",
        "date": "2025-10-03",
        "source": "Press release",
        "analysis": {
            "main_point": "Strategic Salesforce partnership with native CRM integration",
            "metrics": "Bi-directional sync, automated triggers, major conference announcement",
            "target": "Enterprise CRM users, sales teams, data-driven organizations",
            "impact": "Strengthens enterprise positioning, creates integration moat, pressures competitors on ecosystem depth"
        }
    }
]

DEMO_CATEGORIZED_UPDATES = [
    {
        **DEMO_PROCESSED_UPDATES[0],
        "category": "Product",
        "category_reasoning": "Launch of new AI-powered feature with technical capabilities",
        "category_confidence": 0.95
    },
    {
        **DEMO_PROCESSED_UPDATES[1],
        "category": "Pricing",
        "category_reasoning": "Direct pricing strategy change with tier restructuring",
        "category_confidence": 0.98
    },
    {
        **DEMO_PROCESSED_UPDATES[2],
        "category": "Product",
        "category_reasoning": "Strategic partnership creating new product integration capability",
        "category_confidence": 0.88
    }
]

DEMO_TOP_UPDATES = [
    {
        **DEMO_CATEGORIZED_UPDATES[2],
        "priority_score": 9,
        "impact_areas": ["roadmap", "positioning", "partnerships"],
        "urgency_level": "high",
        "strategic_implication": "Major enterprise play that strengthens competitive moat through ecosystem integration"
    },
    {
        **DEMO_CATEGORIZED_UPDATES[0],
        "priority_score": 8,
        "impact_areas": ["roadmap", "product", "positioning"],
        "urgency_level": "high",
        "strategic_implication": "AI-native feature sets new market expectation, requires product roadmap response"
    },
    {
        **DEMO_CATEGORIZED_UPDATES[1],
        "priority_score": 7,
        "impact_areas": ["pricing", "positioning"],
        "urgency_level": "medium",
        "strategic_implication": "Premium pricing increase validates higher willingness-to-pay for automation features"
    }
]

DEMO_DIGEST = """# 🧭 CompetitiveRadar – Weekly Digest
**For:** Tech Startup Founder | **Date:** October 04, 2025

---

## 🔥 Top Competitive Insights This Week

### 1. 🤝 **Airtable Locks In Salesforce Partnership** | Product
Competitor F (Airtable) just announced a major strategic partnership with Salesforce, featuring native bi-directional CRM integration and automated workflow triggers. The announcement was made at a major industry conference with significant media coverage, signaling a serious enterprise push.

**Why it matters:** This creates a powerful integration moat that will be hard to replicate. Enterprise customers now have a seamless path from CRM to workflow automation, strengthening Airtable's position in the sales operations space.

---

### 2. 🤖 **NotionAI Ships AI-Powered Analytics Dashboard** | Product  
Competitor A (NotionAI) launched an AI-powered dashboard that automatically generates insights from workspace data. The feature uses machine learning to identify productivity patterns and suggest optimizations. Early beta users are reporting a 40% efficiency increase.

**Why it matters:** This sets a new bar for AI-native features in productivity tools. Customers will start expecting intelligent, proactive insights rather than passive data storage. This is a roadmap forcing function.

---

### 3. 💰 **ClickUp Raises Enterprise Pricing 31%** | Pricing
Competitor B (ClickUp) increased their enterprise tier from $19/user to $25/user—a 31% jump. The new pricing bundles advanced automation and priority support. They're grandfathering existing customers for 6 months.

**Why it matters:** This validates that enterprise customers will pay premium prices for automation capabilities. It also creates a pricing gap opportunity for competitors who can deliver similar value at the old $19 price point.

---

## 💡 **Founder Takeaway**

**Immediate Actions:**
1. **Partnerships** → Evaluate strategic integration opportunities with major platforms (CRM, communication tools). Ecosystem depth is becoming a competitive requirement for enterprise deals.

2. **Product Roadmap** → Prioritize AI-native features that provide proactive insights, not just reactive data. The market expectation has shifted from "storage + search" to "intelligence + recommendations."

3. **Pricing Strategy** → Review your enterprise pricing model. ClickUp's 31% increase validates premium pricing for automation. Consider whether you're capturing the value you deliver, especially if you have automation features.

**Strategic Insight:** The market is bifurcating into AI-native platforms with deep integrations (premium) vs. traditional tools (commodity). Position accordingly within the next 2 quarters.

---

*Generated by CompetitiveRadar Agentic AI System*
"""
