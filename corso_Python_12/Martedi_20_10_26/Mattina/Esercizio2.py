import numpy as np

scelta = input("Vuoi sovrascrivere il file TXT? (Si/No): ")  #richiesta all'utente se sovrascrivere il file o aggiungere i dati

if scelta == "Si" or scelta == "si":
    modalita = "w"  #apertura del file in modalità scrittura, cancellando i dati precedenti
else:
    modalita = "a"  #apertura del file in modalità aggiunta, mantenendo i dati precedenti

numero_giri = int(input("Quanti giri vuoi eseguire? "))  #richiesta del numero di ripetizioni del processo

for i in range(numero_giri):  #ripetizione del processo per il numero di giri richiesto

    arr = np.linspace(0, 10, 50)  #generazione di un array con 50 numeri equidistanti tra 0 e 10
    print("Array generato:\n", arr)
    print("----------------------------------------------")
    random_array = np.random.uniform(0, 1, (50))  #generazione di un array con 50 numeri casuali tra 0 incluso e 1 escluso
    print("Array casuale:\n", random_array)
    print("----------------------------------------------")
    somma_array = arr + random_array  #somma elemento per elemento dei due array
    print("Somma dei due array:\n", somma_array)
    print("----------------------------------------------")
    sum_value = np.sum(somma_array)  #calcolo della somma di tutti gli elementi del nuovo array
    print("Somma totale:", sum_value)
    print("----------------------------------------------")
    sum_value_maggiore = np.sum(somma_array[somma_array > 5])  #somma degli elementi maggiori di 5 tramite Boolean Indexing
    print("Somma degli elementi maggiori di 5:", sum_value_maggiore)
    print("----------------------------------------------")
    with open("corso_Python_12/Martedi_20_10_26/Mattina/IMPORTO_ESERCIZIO2.txt", modalita) as file:  #apertura del file nella modalità scelta dall'utente
        file.write(str(sum_value) + "\n")  #salvataggio della somma totale nel file TXT
        file.write(str(sum_value_maggiore) + "\n")  #salvataggio della somma degli elementi maggiori di 5

    modalita = "a"  #dopo il primo giro, aggiunta dei risultati successivi senza cancellare quelli già salvati

    print("--------------------------------------")
