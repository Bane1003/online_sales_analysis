import pandas as pd
import nltk

from nltk.sentiment import SentimentIntensityAnalyzer

'''
# Lista pozitivnih reči
positive_words = ["good", "great", "excellent", "amazing","love", "happy", "fantastic"
                  , "perfect", "recommend"]

# Lista negativnih reči
negative_words = ["bad", "terrible", "awful", "worst", "hate","poor", "disappointing", "slow",
    "broken"]'''


# Funkcija za klasifikaciju sentimenta
def classify_sentiment(text):
      text = str(text).lower()

      nltk.download("vader_lexicon")

      '''positive_count = sum(word in text for word in positive_words)
      negative_count = sum(word in text for word in negative_words)

      if positive_count >= negative_count:
              return "positive"
      elif negative_count > positive_count:
              return "negative"'''
        
      result = SentimentIntensityAnalyzer().polarity_scores(text)
      print(result)


# Učitavanje podataka
df = pd.read_csv("data/reviews_labeled_cleaned.csv")

#novi sentiment koji mi pravimo
df['predicted_sentiment']=df['review'].apply(classify_sentiment)

#sacuvaj u okviru novog fajla
df.to_csv("data/reviews_with_predicted_sentiment_V2.csv", index=False)