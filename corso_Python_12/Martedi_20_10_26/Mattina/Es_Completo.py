import numpy as np  #importazione della libreria NumPy per lavorare con gli array

arr=np.arange(50)  #generazione di un array con numeri da 0 a 49
random_array=np.random.randint(49,101,50)  #generazione di un array con 50 numeri casuali da 49 a 100

print("La prima parte dell'array generato è: \n",arr)  #stampa del primo array

print("--------------------------------------")
print("La seconda parte dell'array generato è: \n",random_array)  #stampa del secondo array

print("--------------------------------------")
array_finale=np.concatenate((arr,random_array))  #concatenazione dei due array in un unico array di 100 elementi
print("L'array finale è: \n",array_finale)  #stampa dell'array concatenato

print("Tipo di dati:", array_finale.dtype)  #visualizzazione del tipo di dato degli elementi dell'array
print("Forma dell'array:", array_finale.shape)  #visualizzazione della forma e del numero di elementi dell'array

print("--------------------------------------")
array_finale = array_finale.astype(float)  #conversione degli elementi dell'array in numeri decimali

print("Tipo di dati:", array_finale.dtype)  #stampa del tipo di dato dopo la conversione
print("Forma dell'array:", array_finale.shape)  #stampa della forma dell'array dopo la conversione

print("I primi 10 elementi sono: \n", array_finale[:10])  #selezione e stampa dei primi 10 elementi dell'array
print("--------------------------------------")

print("Gli ultimi 7 elementi dell'array sono: \n", array_finale[-7:])  #selezione e stampa degli ultimi 7 elementi dell'array
print("--------------------------------------")

print("Gli elementi dalla 5 posizione alla 20 escluso sono: \n", array_finale[5:20])  #selezione degli elementi dagli indici 5 a 19 inclusi
print("--------------------------------------")

print("Gli elementi in ogni quarta posizione sono: \n", array_finale[::4])  #selezione degli elementi saltando ogni volta 3 posizioni
print("--------------------------------------")

array_finale[10:15]=999  #sostituzione con il valore 999 degli elementi agli indici da 10 a 14 inclusi
print("L'array dopo la modifica è: \n", array_finale)  #stampa dell'array dopo la modifica
print("--------------------------------------")

indices=np.array([0,3,7,12,25,33,48])  #creazione di un array contenente gli indici degli elementi da selezionare
print("Gli elementi dell'indice richiesto sono: \n",array_finale[indices])  #selezione e stampa degli elementi nelle posizioni indicate
print("--------------------------------------")

for i in array_finale:  #ciclo per scorrere gli elementi dell'array
    print("Gli elementi pari dell'array sono: \n",array_finale[array_finale % 2 == 0])  #selezione e stampa degli elementi divisibili per 2
    break  #interruzione del ciclo dopo la prima iterazione
print("--------------------------------------")

media=np.mean(array_finale)  #calcolo della media aritmetica di tutti gli elementi dell'array
print("Gli elementi maggiori della media sono: \n",array_finale[array_finale>media])  #selezione e stampa degli elementi maggiori della media
