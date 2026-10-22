import pandas as pd

df=pd.read_csv("corso_Python_14/Giovedi_22_10_26/Mattina/statistiche_vendite_settembre_2026.csv")   #Leggiamo il file csv
print(df)

print("------------------------------------------------")

pivot = pd.pivot_table(df, values="Vendite", index="Citta", columns="Prodotto", aggfunc="sum")  #Creiamo una tabella pivot nella quale andiamo a prendere i valori delle vendite
print(pivot)                                                                                    #e in base alla città fa la somma totale di tali prodotti

print("------------------------------------------------")

vendite_totali = df.groupby("Prodotto")["Vendite"].sum()        #Raggruppiamo il valore totale delle vendite di ogni prodotto
print(vendite_totali)