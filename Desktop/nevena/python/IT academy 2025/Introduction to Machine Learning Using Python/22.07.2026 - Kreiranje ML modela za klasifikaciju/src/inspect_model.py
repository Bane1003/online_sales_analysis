import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

model : LogisticRegression = joblib.load("model/sentiment_model.joblib")
vectorizer : TfidfVectorizer = joblib.load("model/tfidf_vectorizer.joblib")

print("Vocabulary size")
print(len(vectorizer.vocabulary_))

print("Vocabulary")
print(vectorizer.get_feature_names_out())

print("Classes: ")
print(model.classes_)

print("Show coeficient matrix shape")
print(model.coef_.shape)

print("Intercept value:")
print(model.intercept_)
