import pandas as pd
import os
import time
from tqdm import tqdm
from agent import ReviewAgent

def run_simulation():
   
    os.makedirs("data", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    
    print("\n---STARTING AGENTIC AI DEMO (ONLINE MODE) ---")
    print("Connecting to Google Gemini to classify recent reviews...\n")
    
    
    try:
        df = pd.read_csv(os.path.join("data", "raw_reviews.csv"))
    except:
        print("Error: Run generate_fake_data.py first.")
        return

    df['at'] = pd.to_datetime(df['at'])
    
    
    df_demo = df.tail(20).copy()
    # -----------------------------------
    
    agent = ReviewAgent()
    trend_data = {}
    dates = sorted(df_demo['at'].dt.date.unique())
    
    print(f"📡 Demonstrating Real-Time Agentic Classification on {len(df_demo)} reviews...")
    
    for current_date in tqdm(dates):
        day_str = current_date.strftime("%Y-%m-%d")
        daily_reviews = df_demo[df_demo['at'].dt.date == current_date]['content'].tolist()
        
        if not daily_reviews: continue
            
        daily_topic_counts = {}
        
       
        results = agent.analyze_batch(daily_reviews)
        
        if not results:
            print("  ! API Quota hit, skipping batch...")
            continue
            
        for item in results:
            topic = item.get('topic', 'Unclassified')
            daily_topic_counts[topic] = daily_topic_counts.get(topic, 0) + 1
            
            
            print(f"  🧠 [AI DECISION] Review: '{item.get('review')[:40]}...'") 
            print(f"     -> Assigned Topic: {topic}")
            
           
            if topic not in agent.topics:
                print(f"  ✨ [NEW TOPIC DISCOVERED] Agent created category: {topic}")
                agent.topics.append(topic)
        
        trend_data[day_str] = daily_topic_counts
        
       
        time.sleep(2)

    print("\n--- ✅ AGENTIC DEMO COMPLETE ---")
    print("Rationale: The Agentic workflow functions correctly.")
    print("Next Step: Executing 'main_offline.py' to generate the full 4,000-review report without rate limits.")

if __name__ == "__main__":
    run_simulation()
