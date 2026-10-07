#Esempi cicli

conteggio = 0

while conteggio < 5:
    print(conteggio)
    conteggio += 1
    
print("----------------------------------------------")   

#Ciclo Booleano
inspettore = True

while inspettore: 
    print("Sei entrato nel dipartimento")
    
    
    scelta=input("Se vuoi uscire dal dipartimento scrivi esci: ")
    if scelta.lower() == "esci":
        inspettore = False
        
print("----------------------------------------------")        
        
#Ciclo for con lista di numeri   
numeri = [1,2,3,4,5,6,7]

for numero in numeri:
    print(numero)
    
print("----------------------------------------------")

#ciclo for con numero iterazioni già deciso
#ciclo for con solo lo start     
for i in range(5):
    print(i)
    
print("----------------------------------------------")  

#ciclo for con start e stop
for i in range(2, 8):
    print(i)
    
print("----------------------------------------------")

#ciclo for con start, stop e step
for i in range(1,10,2):
    print(i)