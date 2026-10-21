import pandas as pd  # importazione della libreria Pandas

# creazione di un dizionario con dati di esempio
data = {
    'Nome': ['Alice', 'Simone', 'Carlo', 'Giulia', 'Marco', 'Sara', 'Luca', 'Elena', 'Matteo', 'Sofia', 'Andrea', 'Chiara', 'Paolo', 'Paolo'],
    'Età': [25, 31, 22, 28, 35, 24, 29, 32, 26, 27, 65, 23, 34, 24],
    'Città': ['Genova', 'Bologna', 'Napoli', 'Milano', 'Roma', 'Torino', 'Firenze', 'Venezia', 'Palermo', 'Bari', 'Verona', 'Pisa', 'Catania', 'Catania'],
    'Salario': [1200, 1500, 1100, 1800, 2200, 1300, 1700, 1900, 1400, None, 2500, 1250, 2100, None]
}

# aggiunta della colonna Categoria Età al dizionario
data['Categoria Età'] = ['Giovane', 'Adulto', 'Giovane', 'Adulto', 'Adulto', 'Giovane', 'Adulto', 'Adulto', 'Adulto', 'Adulto', 'Senior', 'Giovane', 'Adulto', 'Giovane']

df = pd.DataFrame(data)  # creazione di un DataFrame a partire dal dizionario

print(df.head())  # stampa delle prime 5 righe
print("-----------------------------------------")
print(df.tail())  # stampa delle ultime 5 righe
print("-----------------------------------------")
print(df.info())  # stampa delle informazioni sul DataFrame
print("-----------------------------------------")
print(df["Salario"].mean())  # calcolo della media dei salari
print("-----------------------------------------")
print(df["Salario"].median())  # calcolo della mediana dei salari
print("-----------------------------------------")
print(df["Salario"].std())  # calcolo della deviazione standard dei salari
print("-----------------------------------------")

df = df.drop_duplicates(subset="Nome")  # eliminazione dei duplicati considerando la colonna Nome
print(df)  # stampa del DataFrame senza duplicati
print("-----------------------------------------")

df["Salario"] = df["Salario"].fillna(df["Salario"].median())  # sostituzione dei salari mancanti con la mediana
print(df)  # stampa del DataFrame con i salari mancanti sostituiti

df.to_csv("corso_Python_13/Mercoledi_21_10_26/Mattina/analisi.csv", index=False)  # salvataggio del DataFrame in un file CSV senza l'indice
