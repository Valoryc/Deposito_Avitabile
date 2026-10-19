import numpy as np

random_array=np.random.randint(1,100,(6,6))  #generazione di un array di numeri casuali da 1 a 100 6x6
print(random_array)

print("--------------------------------------------------")

print("La sottomatrice 4x4 è: \n", random_array[1:5, 1:5])    #metodo per la sotto matrice 4x4

print("--------------------------------------------------")

print("L'inversione delle righe: \n", random_array[::-1,:]) #metodo per invertire la matrice cambiando l'ultima posizione alla prima e così via

print("--------------------------------------------------")

matrice_invertita = random_array[::-1, :]   #inversione matrice
diagonale = np.diag(matrice_invertita)  #metodo per la creazione della diagonale della matrice invertita
print("La diagonale è ",diagonale)

print("--------------------------------------------------")

for i in random_array:
    random_array[random_array % 3 == 0] = -1    #metodo per verificare tutti i numeri all'interno della matrice invertita e
                                                #nel caso fossero multipli di 3, i loro valore sarà -1
    
print("Matrice modificata: \n",random_array)