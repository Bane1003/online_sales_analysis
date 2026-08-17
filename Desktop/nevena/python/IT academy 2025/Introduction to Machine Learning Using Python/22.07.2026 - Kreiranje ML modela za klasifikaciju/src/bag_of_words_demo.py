from sklearn.feature_extraction.text import CountVectorizer

corpus = [
      "I love this product",
      "This product is not good",
      "Absolutely fantastic experience",
      "Terrible, I hate it",
      "Not great, not terrible"
]

#fit transform uci vokabular i transformise tekstu u vektor

bow_vectorizer=CountVectorizer()
X_bow=bow_vectorizer.fit_transform(corpus)

#get_feature_names_out daje sve reci iz vokabulara
print("Vocabulary:", bow_vectorizer.get_feature_names_out())

#stampanje numerickih vrednosti, da ih vidimo
print("\nBoW Matrix (Document-Term Matrix):\n",X_bow.toarray())