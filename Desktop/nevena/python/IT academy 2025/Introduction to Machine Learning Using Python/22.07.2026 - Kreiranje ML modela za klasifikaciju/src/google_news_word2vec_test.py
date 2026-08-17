import gensim.downloader as api

#postavi se ime modela koji zelimo da skinemo, prethodno je istrenirani model
model = api.load("word2vec-google-news-300")

#5 najslicnijih reci, reci king
#similar_words=model.most_similar('duck',topn=5)
#vector = model['love']
#print(vector)

#print(similar_words)

#uporedjivanje dve reci koliko su slicne
'''similarity1 = model.similarity('king','queen')
print(similarity1)

similarity2 = model.similarity('pear','computer')
print(similarity2)'''

#vrsenje aritmetickih operacija nad recima
#mozemo zato sto su reci pretvorene u vektore

#trazimo najslicnije reci, ali imamo pozitivni primeri i negativni primeri, topn=1 daj nam samo jednu rec
#result = model.most_similar(positive=['Paris','Serbia'], negative=['France'],topn=1)
#print(result)

result = model.most_similar(positive=['woman','king'], negative=['men'],topn=1)
print(result)