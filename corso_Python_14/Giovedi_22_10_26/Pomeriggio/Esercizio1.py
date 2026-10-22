import pandas as pd  # Importa Pandas per lavorare con i dati
import matplotlib.pyplot as plt  # Importa Matplotlib per creare i grafici

df = pd.read_csv("corso_Python_14/Giovedi_22_10_26/Pomeriggio/visitatori_parco_365_giorni.csv")  # Legge il file CSV e crea un DataFrame

print(df.columns)  # Stampa i nomi delle colonne presenti nel file

df['date'] = pd.to_datetime(df['date'])  # Converte la colonna date in formato data
df = df.set_index('date')  # Imposta la data come indice del DataFrame

media = df['visitatori'].mean()  # Calcola la media giornaliera dei visitatori
print("La media dei visitatori è ", media)  # Stampa la media calcolata

deviazione = df['visitatori'].std()  # Calcola la deviazione standard dei visitatori
print("La deviazione è ", deviazione)  # Stampa la deviazione standard

print(df.head())  # Mostra le prime 5 righe del DataFrame
print(df.info())  # Mostra informazioni su colonne, tipi di dati e valori presenti

plt.figure()  # Crea una nuova figura per il grafico
plt.plot(df.index, df['visitatori'])  # Disegna il numero di visitatori giorno per giorno
plt.title("Numero di visitatori giorno per giorno")
plt.show()  # Visualizza il grafico

df['media_mobile'] = df['visitatori'].rolling(7).mean()  # Calcola la media mobile su 7 giorni
plt.figure()  # Crea una nuova figura per il secondo grafico
plt.plot(df.index, df['visitatori'])  # Disegna i visitatori giornalieri
plt.plot(df.index, df['media_mobile'])  # Aggiunge la linea della media mobile
plt.title("Calcolo media su 7 giorni")
plt.show()  # Visualizza il grafico con entrambe le linee

media_mensile = df['visitatori'].resample('ME').mean()  # Calcola la media dei visitatori per ogni mese
plt.figure()  # Crea una nuova figura per il grafico mensile
plt.bar(media_mensile.index, media_mensile)  # Crea un grafico a barre delle medie mensili
plt.title("Media di visitatori per ogni mese")
plt.show()  # Visualizza il grafico delle medie mensili

deviazione_mensile = df['visitatori'].resample('ME').std()  # Calcola la deviazione standard per ogni mese
print(deviazione_mensile)  # Stampa la deviazione standard mensile
