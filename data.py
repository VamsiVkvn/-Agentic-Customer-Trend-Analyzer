import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import random

def generate_complex_reviews():
    start_date = datetime(2024, 6, 1)
    end_date = datetime(2025, 12, 30)
    days = (end_date - start_date).days
    
    data = []
    print("Generating 2500 long, complex reviews...")
    issues = [
        ("Refund Refusal", "I have been waiting for my refund for over 2 weeks now. The customer support keeps closing my ticket without resolution. This is essentially theft. I cancelled my ticket well in advance."),
        ("Hidden Charges", "The app showed a price of 500 when booking, but at the payment gateway it suddenly added a 'convenience fee' and 'agent fee' making it 850. This is deceptive pricing and completely unacceptable."),
        ("App Crash on Payment", "Every time I reach the final payment step, the app freezes and crashes. I have updated to the latest version and cleared cache but the bug persists. I lost my booking chance because of this."),
        ("PNR Status Lag", "The PNR status shown in the app is delayed by 2 hours compared to the official railway website. I almost missed my train because it showed 'Waiting' when it was actually 'Confirmed'."),
        ("Login Loop", "I am stuck in an infinite login loop. I enter the OTP, it says success, and then throws me back to the phone number screen. I cannot access my tickets or my wallet money."),
        ("Excessive Ads", "The amount of popup ads is ridiculous. I accidentally clicked an ad while trying to check my train status. It ruins the user experience completely. Please reduce the ad frequency."),
        ("Battery Drain", "Since the last update, this app consumes 40% of my battery just running in the background. My phone heats up whenever I open the tracking feature. Please optimize the code."),
        ("Wrong Train Location", "The live train tracking is completely inaccurate. It showed the train was 20km away, but the train had already left the station. I missed my train due to this misleading information."),
        ("Wallet Deduction Error", "Money was deducted from my bank account but the ticket was not booked. The money hasn't been refunded to my Ixigo money wallet either. Transaction ID #8829102."),
        ("Customer Support Rude", "I spoke to an agent regarding my cancellation and they were extremely rude and unhelpful. They hung up on me while I was explaining the technical glitch I faced."),
        ("UI/UX Confusing", "The new interface update is terrible. It is so hard to find the 'My Bookings' section now. Why change something that was working perfectly fine? The fonts are also too small."),
        ("Server Timeout", "Keep getting 'Server Request Timed Out' error whenever I search for trains between Delhi and Mumbai. My internet connection is fine (WiFi). Is your backend down?"),
        ("Tatkal Booking Failure", "The app is too slow for Tatkal. By the time the page loads, all tickets are gone. Other apps are much faster. You need to improve the latency for peak hours."),
        ("Appreciation", "Honestly the best travel app out there. The UI is smooth, refunds are instant usually, and the prediction feature is 99% accurate. Love the dark mode feature as well."),
        ("Feature Request", "Please add a feature to book retiring rooms directly from the app. It would be very helpful for long journeys. Also allow us to order food on train via the app.")
    ]

    for _ in range(2500):
        random_days = random.randint(0, days)
        review_date = start_date + timedelta(days=random_days)
        topic, text = random.choice(issues)
        variations = [
            f"Review: {text} Really disappointed.",
            f"Feedback: {text} Fix this immediately.",
            f"{text} This has happened twice now.",
            f"{text}"
        ]
        final_text = random.choice(variations)
        
        data.append({
            'content': final_text,
            'score': random.randint(1, 5),
            'at': review_date
        })
        
    df = pd.DataFrame(data)
    df = df.sort_values(by='at')
    
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/raw_reviews.csv", index=False)
    print("SUCCESS: specific 'raw_reviews.csv' created with long text.")

if __name__ == "__main__":
    generate_complex_reviews()