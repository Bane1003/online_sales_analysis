import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


df = pd.read_csv("data/reviews_labeled_cleaned.csv")

#ulazne karakteriske i ciljna karakteristika
X=df['review']
y=df['sentiment']

#podela podatak na one za treniranje i testiranje
#test_size=0.2 20% ide za test, a 80% za trening
#stratify omogucava da se ocuva raspored klasa u oba skupa podataka
#stratify omogucava da bude ista raspodela pazitivnih i negativnih recenzija
#random_state=42 da podaci budu nasumicno isti svaki put kad pustimo program ponovo
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, stratify=y, random_state=42)

# Display sizes of the resulting sets
print("Training set size:", len(X_train))
print("Test set size:", len(X_test))

# Display class distribution in the training and test sets
print("Training set class distribution:")
print(y_train.value_counts())
print("Test set class distribution:")
print(y_test.value_counts())

#pretvaranjae podataka u brojeve
#ngram_range=(1,2) u recnik se prave kombinacije od jedne i dve reci
#min_df=2 rec mora najmanje dva puta da se ponovo, 
#da bi usla u vokabular
vectorizer = TfidfVectorizer(ngram_range=(1,2), min_df=2)
#ucenje vokabulara, to se vrsi samo jednom
#fit_transform se koristi kada vectorizer uci vokabular
X_train_tfidf = vectorizer.fit_transform(X_train)

#prazan model, ljustura modela
#trenira se model koriscenjem nekog algoritma (LogisticRegression)
model = LogisticRegression()

#dodavanje podataka u model
model.fit(X_train_tfidf, y_train)

joblib.dump(model, "model/sentiment_model.joblib")
joblib.dump(vectorizer, "model/tfidf_vectorizer.joblib")

print("Model and vectorizer are saved.")
'''
print("\nModel is redy.")

while True:

      user_review = input("Enter a review(exit): ")

      if user_review == "exit":
            break

      user_review_tfidf=vectorizer.transform([user_review])

      #predvidjanje modela
      prediction = model.predict(user_review_tfidf)

      print(prediction)'''