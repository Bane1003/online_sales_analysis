from openai import OpenAI
import json

client = OpenAI()

review=input("Please enter review: ")

#promp je ono sto vracamo modelu
prompt=f"Radis kao alat za klasifikaciju recenzija. U nastavku ti dajem recenziju a ti utvrdi njen sentiment (positive, negative, neutral). Pored kategorije, potrebno je da uradis i koeficijent sentimenta, numericku vrednost izmedju 0 i 1, gde je 0 potpuno negativna recenzija, a 1 potpuno pozitivna. Format u kome treba da isporucis odgovor neka bude JSON sa dva kljuca: category i value. Recenzija: \"{review}\""



responses=client.responses.create(model="gpt-5.4-mini", input=prompt)
data = json.loads(responses.output_text)
print(data["category"])
print(data["value"])
