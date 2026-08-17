import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


import pandas as pd

model : LogisticRegression = joblib.load("model/sentiment_model.joblib")
vectorizer : TfidfVectorizer = joblib.load("model/tfidf_vectorizer.joblib")

df = pd.read_csv("data/reviews_labeled_cleaned.csv")

X=df['review']
y=df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, stratify=y, random_state=42)

#ovde se koristi transform, samo pretvara tekst podatke u vektore, numericke podatke
X_test_tfid=vectorizer.transform(X_test)

#model pravi predvidjanje
y_pred=model.predict(X_test_tfid)

#evaluacija
#tacnost
print("Accuracy:", accuracy_score(y_test,y_pred))

#klasifikacioni izvestaj
print("Classification Report:", classification_report(y_test,y_pred))

#matrica zabune
print("Confusion Matrix:", confusion_matrix(y_test,y_pred))
