import numpy as np  #importazione della libreria NumPy

array=np.random.uniform(1,101,(15))  #generazione di un array con 15 numeri casuali tra 1 e 101
array = array.astype(int)  #conversione dei numeri decimali in interi

arr = np.arange(1, 26).reshape(5, 5)  #creazione di una matrice 5x5 con numeri da 1 a 25

array1=np.random.uniform(10,50,(5,5))  #generazione di una matrice 5x5 con numeri casuali tra 10 e 50
array1 = array1.astype(int)  #conversione dei numeri decimali in interi


print("------------MENU------------")
print("BENVENUTO, SCEGLI LA TUA OPERAZIONE!")  #stampa del menu

scelta = int(input("1 Stampa array, 2 Somma e media, 3 Visualizza matrice e colonne, 4 Visualizza righe e diagonale, 5 Fancy Indexing, 6 Modifica elementi, 7 Salva risultati su file TXT, 8 Esci: "))

while scelta != 8:  #ripetizione del menu finché non viene scelta l'opzione 8

    if scelta == 1:
        print("\n",array)  #stampa dell'array
        print("------------------------------")

    elif scelta == 2:
        sum_value = np.sum(array)  #calcolo della somma di tutti gli elementi dell'array
        print("Somma dell'array:", sum_value)  #stampa della somma

        mean_valure = np.mean(array)  #calcolo della media degli elementi dell'array
        print("Media dell'array:", mean_valure)  #stampa della media
        print("------------------------------")

    elif scelta == 3:
        print(arr)  #stampa della matrice

        matrice_colonne = arr[:, 1]  #selezione di tutti gli elementi della seconda colonna
        print("Seconda colonna:", matrice_colonne)  #stampa della colonna
        print("------------------------------")

    elif scelta == 4:
        matrice_righe = arr[3, :]  #selezione di tutti gli elementi della quarta riga
        print("Terza riga:", matrice_righe)  #stampa della riga

        diagonale = arr.diagonal()  #selezione degli elementi della diagonale principale
        print("Diagonale:", diagonale)  #stampa della diagonale

        sum_diagonale = np.sum(diagonale)  #calcolo della somma degli elementi della diagonale
        print("Somma della diagonale:", sum_diagonale)  #stampa della somma
        print("------------------------------")

    elif scelta == 5:
        print(array1)  #stampa della matrice casuale

        print("Elementi selezionati:", array1[[0, 1, 2, 3], [1, 3, 2, 0]])  #selezione degli elementi agli indici indicati

        print("Righe dispari: \n", array1[[1, 3], :])  #selezione delle righe con indici dispari
        print("------------------------------")

    elif scelta == 6:
        array[[0, 1, 2, 3]] += 10  #aggiunta di 10 agli elementi dell'array agli indici 0, 1, 2 e 3
        print("Array modificato: \n", array)  #stampa dell'array modificato
        print("------------------------------")

    elif scelta == 7:
        with open("corso_Python_12/Martedi_20_10_26/Pomeriggio/RISULTATI.txt", "a") as file:  #apertura del file in modalità append
            file.write("Array:\n")  #scrittura del titolo nel file
            file.write(str(array) + "\n")  #salvataggio dell'array
            file.write("Somma dell'array:\n")  #scrittura del titolo della somma
            file.write(str(np.sum(array)) + "\n")  #salvataggio della somma
            file.write("Media dell'array:\n")  #scrittura del titolo della media
            file.write(str(np.mean(array)) + "\n")  #salvataggio della media
            file.write("Matrice arr:\n")  #scrittura del titolo della matrice
            file.write(str(arr) + "\n")  #salvataggio della matrice
            file.write("Diagonale:\n")  #scrittura del titolo della diagonale
            file.write(str(arr.diagonal()) + "\n")  #salvataggio della diagonale
            file.write("Matrice array1:\n")  #scrittura del titolo della seconda matrice
            file.write(str(array1) + "\n")  #salvataggio della seconda matrice
            file.write("Elementi selezionati con Fancy Indexing:\n")  #scrittura del titolo
            file.write(str(array1[[0, 1, 2, 3], [1, 3, 2, 0]]) + "\n")  #salvataggio degli elementi selezionati

        print("Risultati salvati nel file RISULTATI.txt")  #conferma del salvataggio
        print("------------------------------")
    
    else:
        print("Selezione sbagliata")

    scelta = int(input("1 Stampa array, 2 Somma e media, 3 Visualizza matrice e colonne, 4 Visualizza righe e diagonale, 5 Fancy Indexing, 6 Modifica elementi, 7 Salva risultati su file TXT, 8 Esci: "))
    #riproposta della scelta all'utente

print("Uscita dal programma.")  #messaggio finale

