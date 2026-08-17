import joblib

model = joblib.load("model/sentiment_model.joblib")
vectorizer = joblib.load("model/tfidf_vectorizer.joblib")

while True:
      user_review = input("Enter a review(exit): ")
      
      if user_review == "exit":
            break
      
      user_review_tfidf = vectorizer.transform([user_review])
      prediction = model.predict(user_review_tfidf)
      print(prediction)