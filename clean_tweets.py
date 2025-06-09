import pandas as pd
import re

# Load the tweets from CSV
df = pd.read_csv("elon_tweets.csv")

def clean_text(text):
    text = str(text)
    text = re.sub(r"http\S+", "", text)             # Remove URLs
    text = re.sub(r"@\w+", "", text)                # Remove mentions
    text = re.sub(r"#\w+", "", text)                # Remove hashtags
    text = re.sub(r"[^\w\s]", "", text)             # Remove punctuation
    text = re.sub(r"\d+", "", text)                 # Remove numbers
    text = text.lower().strip()                     # Lowercase and trim
    return text

# Apply the cleaning function
df["clean_text"] = df["text"].apply(clean_text)

# Save cleaned tweets to a new file
df.to_csv("cleaned_elon_tweets.csv", index=False)
print("✅ Cleaned tweets saved to cleaned_elon_tweets.csv")
