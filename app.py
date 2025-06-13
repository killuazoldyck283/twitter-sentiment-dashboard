import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import os
import tweepy

# Download VADER lexicon if not already present
nltk.download('vader_lexicon')

# Initialize VADER
sid = SentimentIntensityAnalyzer()

# Load Twitter API keys from environment variables (make sure you’ve set them)
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

# Authenticate with Twitter API
client = tweepy.Client(bearer_token=bearer_token)

# Function to clean tweet text (basic)
def clean_tweet(text):
    return text.replace('\n', ' ').strip()

# Function to fetch tweets
def get_tweets(query, max_tweets=100):
    response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at', 'text', 'lang'])
    tweets = response.data
    if tweets:
        return [clean_tweet(tweet.text) for tweet in tweets if tweet.lang == 'en']
    return []

# Function to analyze sentiment
def analyze_sentiment(tweets):
    results = []
    for tweet in tweets:
        score = sid.polarity_scores(tweet)
        compound = score['compound']
        sentiment = 'Positive' if compound > 0.05 else 'Negative' if compound < -0.05 else 'Neutral'
        results.append({'tweet': tweet, 'sentiment': sentiment})
    return pd.DataFrame(results)

# Streamlit UI
st.title("🐦 Twitter Sentiment Dashboard")
st.write("Analyze sentiment of live tweets using VADER NLP")

# User input
query = st.text_input("Enter a keyword or hashtag to search tweets (e.g. #AI)", "")

if st.button("Analyze"):
    if not query:
        st.warning("Please enter a valid keyword.")
    else:
        with st.spinner("Fetching tweets and analyzing..."):
            tweets = get_tweets(query)
            if not tweets:
                st.error("No tweets found or error with Twitter API.")
            else:
                df = analyze_sentiment(tweets)

                # Show raw data
                st.subheader("Sample Tweets with Sentiment")
                st.dataframe(df.head(10))

                # Sentiment distribution
                sentiment_counts = df['sentiment'].value_counts()
                st.subheader("Sentiment Distribution")
                st.bar_chart(sentiment_counts)

                # Pie chart
                fig, ax = plt.subplots()
                ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
                ax.axis('equal')
                st.pyplot(fig)

                st.success(f"Analyzed {len(df)} tweets.")

