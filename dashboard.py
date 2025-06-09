import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the sentiment data
df = pd.read_csv("sentiment_elon_tweets.csv")

# 🧼 Clean & preprocess datetime (add this line if not already parsed)
df["created_at"] = pd.to_datetime(df["created_at"])


# Page title
st.title("📊 Elon Musk Tweet Sentiment Dashboard")

# 🔍 Search Functionality
st.subheader("🔍 Search Tweets")
search_term = st.text_input("Enter keyword to search:")
if search_term:
    results = df[df["clean_text"].str.contains(search_term.lower())]
    st.write(f"Found {len(results)} tweets:")
    st.write(results[["clean_text", "sentiment"]].head(10))


# Summary stats
st.subheader("Summary")
st.write(f"Total tweets analyzed: {len(df)}")
sentiment_counts = df["sentiment"].value_counts()
st.write(sentiment_counts)

# Bar chart
st.subheader("Sentiment Distribution")
fig, ax = plt.subplots()
sentiment_counts.plot(kind="bar", color=["green", "gray", "red"], ax=ax)
plt.xticks(rotation=0)
st.pyplot(fig)

# Pie chart
st.subheader("Sentiment Pie Chart")
fig2, ax2 = plt.subplots()
ax2.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", colors=["green", "gray", "red"])
ax2.axis("equal")
st.pyplot(fig2)

# 📈 Time Trend — add this block here:
st.subheader("Sentiment Over Time")
daily_sentiment = df.groupby([df["created_at"].dt.date, "sentiment"]).size().unstack().fillna(0)
fig3, ax3 = plt.subplots(figsize=(8, 4))
daily_sentiment.plot(ax=ax3)
plt.xticks(rotation=45)
st.pyplot(fig3)




# Show sample tweets
st.subheader("Sample Tweets by Sentiment")
option = st.selectbox("Choose a sentiment", ["Positive", "Neutral", "Negative"])
sample = df[df["sentiment"] == option].head(5)
st.write(sample[["clean_text"]])

