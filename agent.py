import os
import time
import google.generativeai as genai
from dotenv import load_dotenv
import json
from google.api_core import exceptions

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)

class ReviewAgent:
    def __init__(self):
        self.model = self._get_working_model()
        self.topics = [
            "App crash/bugs",
            "Flight booking issue",
            "Refund delay",
            "Train PNR status issue",
            "Login/OTP problems",
            "Good service/Appreciation"
        ]
        
    def _get_working_model(self):
        try:
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    if 'flash' in m.name: return genai.GenerativeModel(m.name)
            return genai.GenerativeModel('gemini-pro')
        except:
            return genai.GenerativeModel('gemini-pro')

    def _generate_with_retry(self, prompt, retries=5):
        for i in range(retries):
            try:
                return self.model.generate_content(prompt)
            except exceptions.ResourceExhausted:
                wait_time = 30 * (i + 1) 
                print(f"\n[Rate Limit Hit] Pausing for {wait_time} seconds before retrying...")
                time.sleep(wait_time)
            except Exception as e:
                print(f"Error: {e}")
                return None
        return None

    def analyze_batch(self, reviews_text):
        if not reviews_text: return []
        
        prompt = f"""
        Taxonomy: {json.dumps(self.topics)}
        Task: Classify reviews. Create NEW topic if needed.
        Reviews: {json.dumps(reviews_text)}
        Output: JSON list only: [{{"review": "...", "topic": "..."}}]
        """
        
        response = self._generate_with_retry(prompt)
        
        if response:
            try:
                clean_text = response.text.replace("```json", "").replace("```", "").strip()
                return json.loads(clean_text)
            except:
                return []
        return []

    def consolidate_topics(self):
        print(f"Consolidating topics...")
        prompt = f"Merge similar topics in this list: {json.dumps(self.topics)}. Return JSON list."
        
        response = self._generate_with_retry(prompt)
        
        if response:
            try:
                clean_text = response.text.replace("```json", "").replace("```", "").strip()
                self.topics = json.loads(clean_text)
                print("Consolidation complete.")
            except:
                pass