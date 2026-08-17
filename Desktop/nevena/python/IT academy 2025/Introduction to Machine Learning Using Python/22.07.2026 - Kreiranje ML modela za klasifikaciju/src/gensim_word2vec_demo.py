from gensim.models import Word2Vec

#word2vec pokusava reci da smesti u vektorskom prostoru
corpus = [
      "I love this product",
      "This product is not good",
      "Absolutely fantastic experience",
      "Terrible, I hate it",
      "Not great, not terrible"
]

#svaku od recenica podelili smo na tokene
sentences = [sentence.lower().replace(","," ").split() for sentence in corpus]

#vector_size=svaka rec ce da ima 100 razlicitih karakteristika
#window velicina konteksta oko posmatrane reci, model ce da posmatra sve reci  koje se nalaze na udaljenosti od 5 reci
#min_count u vokabular ukljuci reci koje se u korpusu javljaju bar jednom
#workers radne niti koje ce biti koriscene za treniranje niti, da koristi vise jezgara da bude brze
model = Word2Vec(sentences,vector_size=100,window=5, min_count=1, workers=4)

#pretvaranje reci u vektorski oblik
vector = model.wv["love"]

print(vector)