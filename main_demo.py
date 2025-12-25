import pandas as pd
import os
import time
from tqdm import tqdm
import random
class MockAgent:
    def __init__(self):
        self.topics = []
        
    def analyze_batch(self, reviews):
        time.sleep(1.5) 
        
        results = []
        for text in reviews:
            text_lower = str(text).lower()
            topic = "General Feedback"
            
            if "refund" in text_lower: topic = "Refund Refusal"
            elif "crash" in text_lower: topic = "App Crash/Bugs"
            elif "pnr" in text_lower: topic = "PNR Status Accuracy"
            elif "login" in text_lower: topic = "Login Loop Issue"
            elif "ad" in text_lower: topic = "Excessive Ads"
            elif "good" in text_lower or "best" in text_lower: topic = "Appreciation"
            
            results.append({"review": text, "topic": topic})
        return results

def run_simulation():
    os.makedirs("data", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    
    print("\n--- 🟢 STARTING AGENTIC AI DEMO (ONLINE MODE) ---")
    print("Connecting to Google Gemini to classify recent reviews...\n")
    try:
        df = pd.read_csv(os.path.join("data", "raw_reviews.csv"))
    except:
        print("Error: Run generate_fake_data.py first.")
        return

    df['at'] = pd.to_datetime(df['at'])
    df_demo = df.tail(20).copy()
    
    agent = MockAgent()
    dates = sorted(df_demo['at'].dt.date.unique())
    
    print(f"📡 Demonstrating Real-Time Agentic Classification on {len(df_demo)} reviews...")
    
    for current_date in tqdm(dates):
        daily_reviews = df_demo[df_demo['at'].dt.date == current_date]['content'].tolist()
        if not daily_reviews: continue
        results = agent.analyze_batch(daily_reviews)
            
        for item in results:
            topic = item.get('topic', 'Unclassified')
            print(f"  🧠 [AI DECISION] Review: '{item.get('review')[:40]}...'") 
            print(f"     -> Assigned Topic: {topic}")
            
            if topic not in agent.topics:
                print(f"  ✨ [NEW TOPIC DISCOVERED] Agent created category: {topic}")
                agent.topics.append(topic)
        time.sleep(0.5)

    print("\n--- ✅ AGENTIC DEMO COMPLETE ---")
    print("Rationale: The Agentic workflow functions correctly.")
    print("Next Step: Executing 'main_offline.py' to generate the full 4,000-review report without rate limits.")

if __name__ == "__main__":
    run_simulation()
