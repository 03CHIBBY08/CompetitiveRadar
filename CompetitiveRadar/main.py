#!/usr/bin/env python3
import json
import os
import random
from datetime import datetime
from agents.research_agent import research_agent
from agents.categorize_agent import categorize_agent
from agents.prioritize_agent import prioritize_agent
from agents.summarize_agent import summarize_agent

DEMO_MODE = os.environ.get('DEMO_MODE', 'true').lower() == 'true'

def simulate_engagement_metrics():
    """Simulate product engagement metrics for demo purposes"""
    return {
        "insights_viewed": random.randint(85, 98),
        "click_through_rate": round(random.uniform(6.5, 9.2), 1),
        "avg_read_time": f"{random.randint(25, 35)} seconds",
        "action_taken_rate": round(random.uniform(15, 25), 1)
    }

def main():
    print("=" * 60)
    print("🚀 COMPETITIVERADAR - Agentic AI System")
    print("   Transforming competitor tracking into actionable insights")
    print("=" * 60)
    
    if DEMO_MODE:
        print("   🎬 Running in DEMO MODE (no API calls)")
    
    print()
    
    # Load competitor updates
    print("📂 Loading competitor data...")
    with open('data/competitor_updates.json', 'r') as f:
        competitor_updates = json.load(f)
    print(f"   Loaded {len(competitor_updates)} competitor updates")
    print()
    
    if DEMO_MODE:
        from demo_data import DEMO_PROCESSED_UPDATES, DEMO_CATEGORIZED_UPDATES, DEMO_TOP_UPDATES, DEMO_DIGEST
        
        # Agent 1: Research (Demo)
        print(" AGENT 1: RESEARCH")
        print("-" * 60)
        print("🔍 Research Agent: Analyzing competitor updates...")
        processed_updates = DEMO_PROCESSED_UPDATES
        print(f"✅ Research Agent: Processed {len(processed_updates)} updates")
        print()
        
        # Agent 2: Categorization (Demo)
        print(" AGENT 2: CATEGORIZATION")
        print("-" * 60)
        print("🏷️  Categorization Agent: Classifying updates...")
        categorized_updates = DEMO_CATEGORIZED_UPDATES
        print(f"✅ Categorization Agent: Classified {len(categorized_updates)} updates")
        print()
        
        # Agent 3: Prioritization (Demo)
        print(" AGENT 3: PRIORITIZATION")
        print("-" * 60)
        print("⚡ Prioritization Agent: Scoring updates by founder impact...")
        top_updates = DEMO_TOP_UPDATES
        print(f"✅ Prioritization Agent: Selected top 3 from {len(categorized_updates)} updates")
        for i, update in enumerate(top_updates, 1):
            print(f"   #{i}: {update['competitor']} - Score: {update['priority_score']}/10")
        print()
        
        # Agent 4: Summarization (Demo)
        print(" AGENT 4: SUMMARIZATION")
        print("-" * 60)
        print("📝 Summarization Agent: Generating digest...")
        digest = DEMO_DIGEST
        print("✅ Summarization Agent: Digest generated successfully")
        print()
    else:
        # Agent 1: Research
        print(" AGENT 1: RESEARCH")
        print("-" * 60)
        processed_updates = research_agent(competitor_updates)
        print()
        
        # Agent 2: Categorization
        print("🤖 AGENT 2: CATEGORIZATION")
        print("-" * 60)
        categorized_updates = categorize_agent(processed_updates)
        print()
        
        # Agent 3: Prioritization
        print("🤖 AGENT 3: PRIORITIZATION")
        print("-" * 60)
        top_updates = prioritize_agent(categorized_updates)
        print()
        
        # Agent 4: Summarization
        print("🤖 AGENT 4: SUMMARIZATION")
        print("-" * 60)
        digest = summarize_agent(top_updates, founder_persona="Tech Startup Founder")
        print()
    
    # Save digest to file
    with open('weekly_digest.md', 'w') as f:
        f.write(digest)
    print("💾 Digest saved to: weekly_digest.md")
    print()
    
    # Display engagement metrics
    print("=" * 60)
    print("📊 ENGAGEMENT METRICS (Simulated)")
    print("=" * 60)
    metrics = simulate_engagement_metrics()
    print(f"   👀 Insights Viewed: {metrics['insights_viewed']}%")
    print(f"   🖱️  Click-Through Rate: {metrics['click_through_rate']}%")
    print(f"   ⏱️  Avg. Read Time: {metrics['avg_read_time']}")
    print(f"   ✅ Action Taken Rate: {metrics['action_taken_rate']}%")
    print()
    
    # Display digest preview
    print("=" * 60)
    print("📄 DIGEST PREVIEW")
    print("=" * 60)
    print(digest)
    print()
    
    print("=" * 60)
    print("✨ CompetitiveRadar Analysis Complete!")
    print("   View full digest in: weekly_digest.md")
    print("=" * 60)

if __name__ == "__main__":
    main()
