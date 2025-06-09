import tweepy
import pandas as pd
import streamlit as st

print("🚀 Starting script...")

# ✅ Load token from secrets (for deployment)
bearer_token = st.secrets["TWITTER_BEARER_TOKEN"]
print("🔐 Bearer Token loaded...")

# 🐦 Set up Tweepy client
client = tweepy.Client(bearer_token=bearer_token)

# 🔍 Search for recent tweets
query = "elon musk -is:retweet lang:en"
...


