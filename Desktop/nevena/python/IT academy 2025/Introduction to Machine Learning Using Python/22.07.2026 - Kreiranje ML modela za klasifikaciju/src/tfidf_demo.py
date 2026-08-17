from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
      "I love this product",
      "This product is not good",
      "Absolutely fantastic experience",
      "Terrible, I hate it",
      "Not great, not terrible"
]

#fit transform uci vokabular i transformise tekstu u vektor
#min_df govori da rec mora da se pojavi u minimum dva dokumenta 
#ngram_range omogucava da uhvatimo bigrame, dve reci spojene

tfidf_vectorizer=TfidfVectorizer(ngram_range=(1,2))#, min_df=2)
X_tfidf=tfidf_vectorizer.fit_transform(corpus)

#get_feature_names_out daje sve reci iz vokabulara
print("Vocabulary:", tfidf_vectorizer.get_feature_names_out())

#stampanje numerickih vrednosti, da ih vidimo
print("\nBoW Matrix (Document-Term Matrix):\n",X_tfidf.toarray())