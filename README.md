# 🐦 Twitter Sentiment Dashboard

This is a Twitter Sentiment Analysis dashboard built using Python and Streamlit. It allows users to enter a search query and view real-time sentiment analysis (positive, negative, neutral) of tweets using the VADER NLP model.

## 🚀 Features

- Fetch live tweets based on a keyword
- Sentiment analysis using VADER
- Visualize results using pie charts and time-series plots
- Streamlit-based interactive dashboard

## 🧰 Tech Stack

- Python
- Streamlit
- Tweepy
- NLTK (VADER)
- Pandas, Matplotlib

## 📦 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/yourusername/twitter-sentiment-dashboard.git
cd twitter-sentiment-dashboard

# Create a virtual environment 
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
