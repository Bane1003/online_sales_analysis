#analiza podataka

import pandas as pd

# Učitavanje podataka
df = pd.read_csv("data/reviews_labeled.csv")

# Broj redova i kolona za reviews_unlabeled
print("reviews_unlabeled:", df.shape)

# Broj nedostajućih vrednosti po kolonama
print("\nNedostajuće vrednosti u reviews_unlabeled:")
print(df.isnull().sum())

# 5 nasumičnih redova iz reviews_unlabeled
print(df['review'].sample(5, random_state=42))

# Prosečna dužina recenzije (broj reči)
df["review_lenght"] = df["review"].apply(lambda x: len(str(x).split()))
average_length = df['review_lenght'].mean()
print(f"Prosečna dužina recenzije: {average_length:.2f} reči")

# Broj recenzija po sentimentu
print(f"Distribucija 'sentiment' vrednosti: {df["sentiment"].value_counts()}")