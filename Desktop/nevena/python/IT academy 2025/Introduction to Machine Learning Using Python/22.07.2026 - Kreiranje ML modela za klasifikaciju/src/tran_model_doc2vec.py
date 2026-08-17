import joblib
import numpy as np
import pandas as pd

from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from gensim.utils import simple_preprocess

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#Load the labeled datset

df=pd.read_csv("data/reviews_labeled_cleaned.csv")

df_train,df_test=train_test_split(df, test_size=0.2, stratify=df['sentiment'], random_state=42)

#Convert training reviews into TaggedDocument objects
#kriraju se objekti kase TaggedDocument
#sve recenzije se dele na reci koriscenjem simple_preprocess
#tags su samo numericke oznake recenzije
tagged_train_reviews = [
      TaggedDocument(
            words=simple_preprocess(review),
            tags=[f"REVIEW_{index}"]
      )
      for index, review in df_train["review"].items()
]

#Create the Doc2Vec model
vectorizer = Doc2Vec(
      vector_size=100,
      window=5,
      min_count=2,
      workers=4,
      epochs=40,
      dm=1,
      seed=42
)

#Build the vocabulary
#izgradjuje se vokabular
vectorizer.build_vocab(tagged_train_reviews)

#Train the Doc2Vec model
#trenira se vectorazier, naucene stvari cuva u okviru vectorizer modela
vectorizer.train(
      tagged_train_reviews,
      total_examples=vectorizer.corpus_count,
      epochs=vectorizer.epochs
)

#Get the learned vectors for training reviews
X_train_doc2vec = np.array([
      vectorizer.dv[f"REVIEW_{index}"]
      for index in df_train.index
])

y_train = df_train['sentiment']

#Train the sentiment classifier
model=LogisticRegression()
model.fit(X_train_doc2vec, y_train)

joblib.dump(model, "model/doc2vec_sentiment_model.joblib")
joblib.dump(vectorizer, "model/doc2vec_vectorizer.joblib")

print("Model and vectorizer are saved.")
