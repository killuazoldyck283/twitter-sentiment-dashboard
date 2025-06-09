import pandas as pd
import matplotlib.pyplot as plt

# Load sentiment data
df = pd.read_csv("sentiment_elon_tweets.csv")

# Count sentiment categories
sentiment_counts = df["sentiment"].value_counts()

# Bar chart
plt.figure(figsize=(6, 4))
sentiment_counts.plot(kind="bar", color=["green", "gray", "red"])
plt.title("Sentiment Analysis of Elon Tweets")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sentiment_bar_chart.png")
plt.show()
