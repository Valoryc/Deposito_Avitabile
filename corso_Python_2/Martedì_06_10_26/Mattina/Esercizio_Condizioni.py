#Esercizio Condizioni

num1 = int(input("Inserisci il numero: "))

if num1 > 0:
    print("Il numero è maggiore di 0")
    
    print("--------------------")
    
    num1 = int(input("Inserisci un numero maggiore di 20: "))
    if num1 >  20:
        
        print("Il numero è maggiore di 20")
        print("--------------------")
        
        num1 = int(input("Inserisci un numero maggiore di 200: "))
        
        if num1 > 200:
            print("Il numero è maggiore di 200")

print("------------------------------------")
            
            
print("--------------------")
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Che cosa vuoi fare? Aggiungere, Modificare o Eliminare?")
num = int(input(" "))

if num == 1:
    num2 = input("Scegli un numero da aggiungere: ")
    numero.append(int(num2))
    print(numero)
    
elif num == 2:
    num2= input("Scegli un numero da modificare: ")
    numero.insert(int(num2), int(input("Inserisci il nuovo numero: ")))
    print(numero)   
    
elif num == 3:
    num2= input("Scegli un numero da eliminare: ")
    numero.remove(int(num2))
    print(numero)

else:
    print("Scelta non valida") 
    
print("--------------------------------------------")
    

    