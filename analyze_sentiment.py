import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the cleaned tweets
df = pd.read_csv("cleaned_elon_tweets.csv")

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to classify sentiment
def get_sentiment(text):
    score = analyzer.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["sentiment"] = df["clean_text"].apply(get_sentiment)

# Save the results to a new CSV
df.to_csv("sentiment_elon_tweets.csv", index=False)
print("🎯 Sentiment analysis complete! Results saved to sentiment_elon_tweets.csv")
