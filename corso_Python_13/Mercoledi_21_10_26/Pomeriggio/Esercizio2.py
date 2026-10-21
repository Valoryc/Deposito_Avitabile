import pandas as pd  # Importo la libreria pandas per lavorare con i dati

df = pd.read_csv("corso_Python_13/Mercoledi_21_10_26/Pomeriggio/cars_con_prezzi_quantita.csv")  # Leggo il file CSV e lo carico nel DataFrame

df["Totale Vendite"] = df["Quantita"] * df["Prezzo Unitario"]  # Calcolo il totale delle vendite moltiplicando quantità e prezzo unitario

print(df)  # Stampo il DataFrame completo

print("-----------------------------------------")

totali = df.groupby("Modello")["Totale Vendite"].sum()  # Raggruppo le auto per modello e sommo le vendite totali di ogni modello
print(totali)  # Stampo il totale delle vendite per ciascun modello

print("-----------------------------------------") 

totali_quantita = df.groupby("Modello")["Quantita"].sum()  # Raggruppo le auto per modello e sommo le quantità
prodotto_venduto = totali_quantita.idxmax()  # Individuo il modello con la quantità totale più alta

print("-----------------------------------------")   

print("In termini di quantità la macchina più venduta è:", prodotto_venduto)  # Stampo il modello con la quantità più alta

vendite_per_marca = df.groupby("Marca")["Totale Vendite"].sum()  # Raggruppo le auto per marca e sommo le vendite totali
marca_migliore = vendite_per_marca.idxmax()  # Individuo la marca con il valore totale delle vendite più alto

print("-----------------------------------------") 

print("Marca con vendite totali più alte:", marca_migliore)  # Stampo la marca con le vendite totali maggiori
print("Valore totale:", vendite_per_marca.max(), "euro")  # Stampo il valore massimo delle vendite

print("-----------------------------------------")  

vendite_gen = df[df["Totale Vendite"] > 3000000]  # Creo un DataFrame con le auto il cui totale supera 3.000.000 di euro
print(vendite_gen)  # Stampo solo le righe che rispettano la condizione

print("-----------------------------------------")  

df_ordinato = df.sort_values(by="Totale Vendite", ascending=False)  # Ordino le auto dal totale delle vendite più alto al più basso
print(df_ordinato)  # Stampo il DataFrame decrescente
