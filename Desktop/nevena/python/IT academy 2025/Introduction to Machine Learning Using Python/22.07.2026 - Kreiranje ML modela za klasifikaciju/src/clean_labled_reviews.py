import pandas as pd

# Učitavanje podataka
df = pd.read_csv("data/reviews_labeled.csv")

#brisanje nedostajucih vrednosti
df=df.dropna()

#pretvaranje u mala slova
df['sentiment']=df['sentiment'].str.strip().str.lower()

#provera jedinstvenosti sentimenta
print(df["sentiment"].unique())

#sacuvati modifikovan fajl
df.to_csv("data/reviews_labeled_cleaned.csv", index=False)