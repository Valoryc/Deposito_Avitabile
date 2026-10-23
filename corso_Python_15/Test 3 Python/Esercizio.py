import pandas as pd
import matplotlib.pyplot as plt

df_data = pd.read_csv("corso_Python_15/Test 3 Python/candy-data.csv")  # legge i dati dei prodotti
df_vendite = pd.read_csv("corso_Python_15/Test 3 Python/candy-vendite.csv")  # legge i dati delle vendite

print(df_data)  # stampa i prodotti

print("-----------------------------------------------")

print(df_vendite)  # stampa le vendite

venditezona=df_vendite["area_vendita"]  # seleziona le aree di vendita
venditeunita=df_vendite["unita_vendute"]  # seleziona le unità vendute

df=pd.merge(df_data, df_vendite, on="competitorname")  # unisce i due dataframe tramite il nome del prodotto

doppio=df_data.drop_duplicates(subset="sugarpercent")  # elimina i duplicati in base alla percentuale di zucchero
print(doppio)

print("-----------------------------------------------")

doppio=df_data.drop_duplicates(subset="pricepercent")  # elimina i duplicati in base alla percentuale del prezzo
print(doppio)

plt.figure()  # crea una nuova figura
plt.xlabel("Area massima delle vendite")  # assegna il nome all'asse x
plt.ylabel("Prodotto massimo comprato")  # assegna il nome all'asse y
plt.bar(venditezona,venditeunita)  # crea il grafico a barre
plt.title("Grafico che controlla il prodotto più acquistato e la zona che l'ha acquistato di più")  # assegna il titolo
plt.show()  # mostra il grafico

print("-----------------------------------------------")

min_prodotto= df_vendite["unita_vendute"].min()  # trova il minimo delle unità vendute
min=df_vendite["competitorname"].min()  # trova il primo nome in ordine alfabetico
zona=df_vendite["area_vendita"].min()  # trova la prima zona in ordine alfabetico
print("Il minimo che è stato prodotto è ", min_prodotto , " del prodotto " , min, " nella zona ", zona)  # stampa i valori trovati

recensione = df_vendite.groupby("area_vendita")["valutazione_clienti"].mean()  # calcola la media delle recensioni per zona
plt.figure()  # crea una nuova figura
plt.xlabel("Area delle recensioni")  # assegna il nome all'asse x
plt.ylabel("Recensioni clienti")  # assegna il nome all'asse y
plt.bar(recensione.index, recensione.values)  # crea il grafico delle recensioni medie
plt.title("Grafico per le recensioni più alte")  # assegna il titolo
plt.show()  # mostra il grafico

print("-----------------------------------------------")
print("La tabella con i valori aggiornati \n")  # stampa il titolo della tabella

df_data["fruity"] = 1  # imposta tutti i valori a 1
  # stampa del DataFrame con l'età mancante sostituita

df_data["chocolate"]=1  # imposta tutti i valori a 1

df_data["caramel"]=1  # imposta tutti i valori a 1

df_data["peanutyalmondy"]=1  # imposta tutti i valori a 1

df_data["nougat"]=1  # imposta tutti i valori a 1

df_data["crispedricewafer"]=1  # imposta tutti i valori a 1

df_data["hard"]=1  # imposta tutti i valori a 1

df_data["bar"]=1  # imposta tutti i valori a 1

df_data["pluribus"]=1  # imposta tutti i valori a 1

print(df_data)  # stampa il dataframe aggiornato