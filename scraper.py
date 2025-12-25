import pandas as pd
from google_play_scraper import Sort, reviews
from datetime import datetime
import os
import sys
APP_ID = 'com.ixigo.train.ixitrain'  
START_DATE = datetime(2025, 4, 1)
def fetch_reviews():
    print(f"Fetching reviews for {APP_ID} from {START_DATE.date()} to now...")
    
    try:
        result = []
        fetched_reviews, _ = reviews(
            APP_ID,
            lang='en', 
            country='in', 
            sort=Sort.NEWEST,
            count=4000 
        )
        result.extend(fetched_reviews)
    except Exception as e:
        print(f"Error connecting to Google Play: {e}")
        sys.exit(1)

    if not result:
        print("ERROR: No reviews found.")
        sys.exit(1)
    df = pd.DataFrame(result)
    
    if 'at' not in df.columns:
        print("Error: 'at' (date) column missing.")
        sys.exit(1)
    df['at'] = pd.to_datetime(df['at'])
    df_filtered = df[df['at'] >= START_DATE]
    df_filtered = df_filtered[['content', 'score', 'at']]
    df_filtered = df_filtered.sort_values(by='at')
    
    if df_filtered.empty:
        print(f"Warning: No reviews found after {START_DATE.date()}. Try increasing 'count' in code.")
        sys.exit(1)
    os.makedirs("data", exist_ok=True)
    output_path = os.path.join("data", "raw_reviews.csv")
    df_filtered.to_csv(output_path, index=False)
    print(f"SUCCESS: Saved {len(df_filtered)} reviews from April 2025 onwards to {output_path}")

if __name__ == "__main__":
    fetch_reviews()