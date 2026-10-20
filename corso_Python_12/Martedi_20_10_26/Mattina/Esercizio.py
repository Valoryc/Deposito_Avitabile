import numpy as np  #importazione della libreria NumPy per lavorare con gli array

arr=np.linspace(0,1,12)  #generazione di un array con 12 numeri equidistanti tra 0 e 1
print ("Array creato \n",arr)  #stampa dell'array generato
print("--------------------------------------")

arr_reshape=arr.reshape(3,4)  #trasformazione dell'array in una matrice con 3 righe e 4 colonne

print("La sottomatrice 3x4: \n", arr_reshape[:,:])  #selezione e stampa dell'intera matrice 3x4
print("--------------------------------------")

sum_value=np.sum(arr_reshape)  #calcolo della somma di tutti gli elementi della matrice
print("La somma della matrice 3x4: \n",sum_value)  #stampa del risultato della somma

print("--------------------------------------")

random_array = np.random.uniform(0, 1, (3, 4))  #generazione di una matrice 3x4 con numeri casuali decimali tra 0 incluso e 1 escluso
print("La generazione della matrice 3x4 con numeri casuali: \n",random_array)  #stampa della matrice casuale
print("--------------------------------------")

sum2_value=np.sum(random_array)  #calcolo della somma di tutti gli elementi della matrice casuale

print("La somma della matrice casuale: \n",sum2_value)  #stampa del risultato della somma
print("--------------------------------------")

array_interi=arr.astype(int)  #conversione degli elementi dell'array originale in numeri interi
print("L'array convertito in numeri interi: \n",array_interi)  #stampa dell'array dopo la conversione
