# Agentic Customer Trend Analyzer

**A Dual-Mode Agentic Workflow for Temporal Topic Modeling on User Reviews.**

This repository contains the solution for the PulseGen "Senior AI Engineer" assignment. It implements an autonomous pipeline to ingest Google Play Store reviews, deduplicate semantic topics, and generate a 6-month trend analysis matrix.

---

## 🚀 Key Features

* **Agentic AI Classification:** Uses Google Gemini (LLM) to semantically classify reviews and discover new evolving topics (e.g., distinguishing "Refund Refusal" from generic "Payment Issues").
* **Dynamic Taxonomy Generation:** Automatically consolidates similar phrases (e.g., "Rude agent", "Bad behavior") into single canonical topics to prevent trend fragmentation.
* **Hybrid Architecture:**
    * **Online Mode:** Real-time agentic reasoning using Gemini API (demonstrated on sample batches).
    * **Offline Mode:** Robust fallback using keyword-based taxonomy to process large datasets (4,000+ reviews) without hitting Free Tier API rate limits.
* **Temporal Trend Matrix:** Outputs a structured report mapping `Date` vs. `Topic Frequency` for product insights.

---

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/VamsiVkvn/-Agentic-Customer-Trend-Analyzer.git](https://github.com/VamsiVkvn/-Agentic-Customer-Trend-Analyzer.git)
    cd -Agentic-Customer-Trend-Analyzer
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas google-generative-ai google-play-scraper tqdm python-dotenv
    ```

3.  **Set up API Key:**
    Create a `.env` file and add your Google Gemini API key:
    ```
    GOOGLE_API_KEY=your_api_key_here
    ```

---

## ▶️ How to Run

### 1. Data Ingestion
Fetch real-time reviews from the Google Play Store or generate a synthetic high-volume dataset for testing:
```bash
# Option A: Scrape Real Data
python scraper.py

# Option B: Generate Synthetic Data (Recommended for full 6-month simulation)
python generate_fake_data.py