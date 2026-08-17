import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from gensim.utils import simple_preprocess
from gensim.models.doc2vec import TaggedDocument
from gensim.models import Doc2Vec
import numpy as np

import pandas as pd

model : LogisticRegression = joblib.load("model/doc2vec_sentiment_model.joblib")
vectorizer : Doc2Vec = joblib.load("model/doc2vec_vectorizer.joblib")

df = pd.read_csv("data/reviews_labeled_cleaned.csv")

df_train,df_test=train_test_split(df, test_size=0.2, stratify=df['sentiment'], random_state=42)

#Convert training reviews into TaggedDocument objects

#Vectorizer svih test recenzija
#simple_preprocess dele se recenzije na reci
X_test_doc2vec = np.array([
      vectorizer.infer_vector(
            simple_preprocess(review),
            epochs=40
      )
      for review in df_test['review']
])

y_test = df_test['sentiment']
y_pred = model.predict(X_test_doc2vec)

#evaluacija
#tacnost
print("Accuracy:", accuracy_score(y_test,y_pred))

#klasifikacioni izvestaj
print("Classification Report:", classification_report(y_test,y_pred))

#matrica zabune
print("Confusion Matrix:", confusion_matrix(y_test,y_pred))
