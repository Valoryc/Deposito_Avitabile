import numpy as np

#non sta creando un array, sta convertendo una lista in un array
lista = [1,2,3]

arr = np.array(lista)


#*************************************************
arr = np.array([1,2,3,4,5,6]) #array UNIDIMENSIONALE
print(arr)

arr2d = np.array([[1,2,3],[4,5,6]]) #array BIDIMENSIONALE
print(arr2d)



# Creazione di un array
arr3d = np.array([[1,2,3],[4,5,6]])


# Utilizzo di alcuni metodi

print("Forma dell'array:", arr3d.shape)  # Output: (2,3) indica le sue dimensioni (non lavorano tra di loro), forma dell'array

print("Dimensioni dell'array:", arr3d.ndim)  # Output: 2

print("Tipo di dati:", arr3d.dtype)  # Output: int64 , specifica il tipo di dati contenuti nell'array

print("Numero di elementi:", arr3d.size)  # Output: 6

print("Somma degli elementi:", arr3d.sum())  # Output: 21

print("Media degli elementi:", arr3d.mean())  # Output: 3.5

print("Valore massimo:", arr3d.max())  # Output: 6

print("Indice del valore massimo:", arr3d.argmax())  # Output: 5


arr4d = np.arange(10)
print("Array contenete sequenza di numeri: ", arr4d) #simile al range di Python, crea un array contenente una sequenza di numeri

arr5d = np.arange(6)
reshape_arr= arr5d.reshape((2,3)) #cambia la forma dell'array senza modificare i dati
print("Array con forma diversa: ", reshape_arr)