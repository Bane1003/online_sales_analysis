from openai import OpenAI
import json
import pandas as pd

client = OpenAI()


# Funkcija za klasifikaciju sentimenta
def classify_sentiment(text):
      prompt=f"Radis kao alat za klasifikaciju recenzija. U nastavku ti dajem recenziju a ti utvrdi njen sentiment (positive, negative, neutral). Pored kategorije, potrebno je da uradis i koeficijent sentimenta, numericku vrednost izmedju 0 i 1, gde je 0 potpuno negativna recenzija, a 1 potpuno pozitivna. Format u kome treba da isporucis odgovor neka bude JSON sa dva kljuca: category i value. Recenzija: \"{text}\""
      responses=client.responses.create(model="gpt-5.4-mini", input=prompt)
      data = json.loads(responses.output_text)
      return (data["category"])


# Učitavanje podataka
df = pd.read_csv("data/reviews_labeled_cleaned.csv")

#novi sentiment koji mi pravimo
df['predicted_sentiment']=df['review'].apply(classify_sentiment)

#sacuvaj u okviru novog fajla
df.to_csv("data/reviews_with_predicted_sentiment_openai.csv", index=False)


