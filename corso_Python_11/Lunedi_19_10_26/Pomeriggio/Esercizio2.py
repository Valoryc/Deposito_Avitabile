import numpy as np

random_array=np.random.randint(10,50,20)        #generazione di un array di soli numeri interi grazie al random.randint
print("L'array generato è: ", random_array)


print("I primi 10 elementi dell'array: ", random_array[:10])        #stampa tutti i numeri fino alla posizione 10

print("Gli utlimi 5 elementi dell'array: ",random_array[-5:])   #parte dalla quintultima posizione ad andare verso la fine

print("Gli elementi nell'indice che va da 5 a 15 (escluso) sono: " , random_array[5:15])    #tutte le posizioni includendo il 5 ed escludendo il 15

print("Tutti gli elementi nelle terze posizioni sono: ", random_array[::3]) #tutti i numeri presenti nella 3 posizione

random_array[5:10]=99   #i numeri nelle posizione che vanno da 5 a 10 vengono cambiati in 99
print("L'array dopo averlo modificato è: ", random_array)

