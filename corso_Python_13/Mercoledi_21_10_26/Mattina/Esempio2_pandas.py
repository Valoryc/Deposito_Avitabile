import pandas as pd

df_scv = pd.read_csv("corso_Python_13/Mercoledi_21_10_26/Mattina/studenti.csv")

#Aggiunta di una colonna
df_scv["Sesso"] = ["M", "M", "F", "F" , "M", "F", "M", "F", "M", "F"]

# crea una colonna Promosso riempiendola di valori booleani in basse alla colonna voto
df_scv["promesso"] = df_scv["voto"]>=6  #BROADCAST 
print(df_scv)
print("")

#stampa la media dei voti
print(df_scv["voto"].mean())
print("")

print(df_scv["voto"].max())
print("")

print(df_scv[df_scv["voto"]>7]) #vettoriale
print("")

#Salvare il dataframe in un nuovo csv
df_scv.to_csv("corso_Python_13/Mercoledi_21_10_26/Mattina/studenti_aggiornato.csv", index=False) #salva i dati ma non l'indice