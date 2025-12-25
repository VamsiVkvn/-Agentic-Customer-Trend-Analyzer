import pandas as pd
import os
from tqdm import tqdm

def get_topic_offline(text):
    text = str(text).lower()
    
    if "refund" in text and "refusal" in text:
        return "Refund Refusal"
    elif "hidden" in text or "deceptive" in text or "convenience fee" in text:
        return "Hidden Charges/Pricing"
    elif "crash" in text and "payment" in text:
        return "App Crash (Payment Stage)"
    elif "pnr" in text and ("lag" in text or "delay" in text):
        return "PNR Status Accuracy"
    elif "loop" in text or "infinite" in text:
        return "Login/OTP Loop Issue"
    elif "ad" in text and ("popup" in text or "frequency" in text):
        return "Excessive Ads"
    elif "battery" in text or "heat" in text:
        return "Performance: Battery Drain"
    elif "location" in text and "wrong" in text:
        return "Live Tracking Inaccuracy"
    elif "deducted" in text and "not booked" in text:
        return "Payment Failure (Money Deducted)"
    elif "agent" in text and ("rude" in text or "hung up" in text):
        return "Customer Support Behavior"
    elif "interface" in text or "font" in text or "confusing" in text:
        return "UI/UX Design Complaint"
    elif "timeout" in text or "server" in text:
        return "Server/Connectivity Issues"
    elif "tatkal" in text and "slow" in text:
        return "Tatkal Booking Latency"
    elif "feature" in text or "add" in text:
        return "New Feature Request"
    elif "best" in text or "love" in text or "smooth" in text:
        return "Appreciation"
    else:
        return "General Feedback"

def run_simulation():
    os.makedirs("data", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    
    print("Running FINAL REPORT GENERATION on Synthetic Data...")
    
    try:
        df = pd.read_csv(os.path.join("data", "raw_reviews.csv"))
    except:
        print("Error: Run generate_fake_data.py first!")
        return

    df['at'] = pd.to_datetime(df['at'])
    trend_data = {}
    dates = sorted(df['at'].dt.date.unique())
    
    print(f"Processing {len(df)} long reviews across {len(dates)} days...")
    
    for current_date in tqdm(dates):
        day_str = current_date.strftime("%Y-%m-%d")
        daily_reviews = df[df['at'].dt.date == current_date]['content'].tolist()
        
        if not daily_reviews: continue
            
        daily_topic_counts = {}
        for review in daily_reviews:
            topic = get_topic_offline(review)
            daily_topic_counts[topic] = daily_topic_counts.get(topic, 0) + 1
            
        trend_data[day_str] = daily_topic_counts

    print("Generating Final Matrix...")
    report_df = pd.DataFrame(trend_data).fillna(0).astype(int)
    report_df = report_df.reindex(sorted(report_df.columns), axis=1)
    
    output_file = os.path.join("output", "trend_report.csv")
    report_df.to_csv(output_file)
    print(f"SUCCESS! Rich Trend Report saved to {output_file}")

if __name__ == "__main__":
    run_simulation()