import numpy as np

arr=np.linspace(0,1,5) #Generiamo un array di numeri equidistanti tra un valore iniziale e uno finale
print (arr)


random_arr=np.random.rand(3,3)  #Genera array di numeri casuali
print(random_arr)


arr=np.array([1,2,3,4])

sum_value=np.sum(arr)
mean_value=np.mean(arr)
std_value=np.std(arr)

print("La somma ", sum_value)
print("La media ", mean_value)

print("Standard Deviation: " , std_value)