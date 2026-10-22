import pandas as pd

iscritti = {
'Nome': ['Marco', 'Giulia', 'Luca', 'Sara', 'Marco', 'Francesca', 'Andrea', 'Elena', None, 'Matteo'],
'Eta': [25, 32, 28, 22, 25, 35, None, 29, 31, 40],
'Citta': ['Napoli', 'Roma', 'Milano', 'Napoli', 'Napoli','Roma', 'Milano', 'Torino', 'Napoli', 'Firenze'],
'Tipo_Abbonamento': ['Base', 'Premium', 'Family', 'Base', 'Base', 'Premium', 'Family', None, 'Base', 'Premium']
}


df_iscritti= pd.DataFrame(iscritti)


presenze = {
'Data': ['2026-10-01', '2026-10-01', '2026-10-01', '2026-10-02', '2026-10-02', '2026-10-02', '2026-10-03', '2026-10-03', '2026-10-03', '2026-10-04', '2026-10-04', '2026-10-04', '2026-10-05', '2026-10-05', '2026-10-05'],
'Corso': ['Yoga', 'Crossfit', 'Nuoto', 'Pilates', 'Yoga', 'Crossfit', 'Nuoto', 'Pilates', 'Yoga', 'Crossfit', 'Nuoto', 'Pilates', 'Yoga', 'Crossfit', 'Nuoto'],
'Citta': ['Napoli', 'Roma', 'Milano', 'Napoli', 'Roma', 'Milano', 'Napoli', 'Roma', 'Milano', 'Napoli', 'Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
'Partecipanti': [12, 15, 20, 10, 14, 18, 22, 11, 16, 13, 19, 9, 17, 21, 24]
}


df_presenze=pd.DataFrame(presenze)

abbonamenti ={
'Tipo_Abbonamento': ['Base', 'Premium', 'Family'],
'Costo_Mensile': [30, 50, 80]   
}

df_abbonamenti=pd.DataFrame(abbonamenti)


df = df_iscritti.drop_duplicates(subset="Nome")  # eliminazione dei duplicati considerando la colonna Nome
print(df)  # stampa del DataFrame senza duplicati

print("----------------------------------------------------")

df_iscritti["Eta"] = df_iscritti["Eta"].fillna(df_iscritti["Eta"].fillna(22))  # sostituzione dei valori mancanti con l'età
print(df_iscritti)  # stampa del DataFrame con l'età mancante sostituita

print("----------------------------------------------------")

df_iscritti["Nome"] = df_iscritti["Nome"].fillna(df_iscritti["Nome"].fillna("Pietro"))  # sostituzione dei valori mancanti con il nome
print(df_iscritti)  # stampa del DataFrame con il nome mancante sostituito

print("----------------------------------------------------")

df_iscritti["Tipo_Abbonamento"] = df_iscritti["Tipo_Abbonamento"].fillna(df_iscritti["Tipo_Abbonamento"].fillna("Base"))  # sostituzione dei valori mancanti con l'abbonamento
print(df_iscritti)  # stampa del DataFrame con l'abbonamento mancante sostituito

print("----------------------------------------------------")

print(df_iscritti["Tipo_Abbonamento"].value_counts()) #Frequenze per abbonamento

print("----------------------------------------------------")

print(df_iscritti["Citta"].value_counts()) #Frequenze per città

print("----------------------------------------------------")

print(df_presenze["Corso"].value_counts()) #Frequenze per corso

print("----------------------------------------------------")

print(df_presenze["Citta"].value_counts()) #Frequenze per città nelle presenze

print("----------------------------------------------------")

report_abbonamenti = df_iscritti['Tipo_Abbonamento'].value_counts() #Verifichiamo quanti iscritti hanno un determinato abbonamento
print(report_abbonamenti)

print("----------------------------------------------------")

report_corsi = df_presenze.groupby("Corso")["Partecipanti"].sum()   #Raggruppiamo tutti i partecipanti di un corso specifico
print(report_corsi)

print("----------------------------------------------------")

report_citta = df_presenze.groupby("Citta")["Partecipanti"].sum()   #Raggruppiamo tutti i partecipanti di tutte e tre le citta
print(report_citta)

print("----------------------------------------------------")

df_report=pd.merge(df_iscritti, df_abbonamenti, on="Tipo_Abbonamento")  #Uniamo gli scritti e gli abbonamenti per un report generale tramite il tipo di abbonamento
print(df_report)
