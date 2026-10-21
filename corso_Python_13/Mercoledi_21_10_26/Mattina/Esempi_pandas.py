import pandas as pd

# Creazione di un DataFrame con dati di esempio
data = {
'Nome': ['Alice', 'Bob', 'Carla'],
'Età': [25, 30, 22],
'Città': ['Roma', 'Milano', 'Napoli']
}

# aggiunta di una chiave al dizionario
data["Sesso"] = ["F","M","F"]

df = pd.DataFrame(data)

# Stampa del DataFrame originale

print("DataFrame Originale:")

print(df)


print(df.head()) #prime 5 righe

print(df.tail())    #ultime 5 righe

print(df.describe())    #descrizione    

print(df.info())    #informazione