import pandas as pd
import nltk

from nltk.sentiment import SentimentIntensityAnalyzer

#nltk.download("vader_lexicon")

'''tweet = 'ITAcademy is a great school to learn machin learning! :)'

#polarity_scores metoda koja daje sentimente
result = SentimentIntensityAnalyzer().polarity_scores(tweet)
print(result)'''


# Funkcija za klasifikaciju sentimenta
def classify_sentiment(text):
      text = str(text).lower()
      
      result=SentimentIntensityAnalyzer().polarity_scores(text)

      if result['compound'] >= 0:
              return "positive"
      else:
              return "negative"
        


# Učitavanje podataka
df = pd.read_csv("data/reviews_labeled_cleaned.csv")

#novi sentiment koji mi pravimo
df['predicted_sentiment']=df['review'].apply(classify_sentiment)

#sacuvaj u okviru novog fajla
df.to_csv("data/reviews_with_predicted_sentiment_vadar.csv", index=False)