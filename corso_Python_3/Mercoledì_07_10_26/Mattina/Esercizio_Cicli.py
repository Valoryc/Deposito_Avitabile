#Esercizi Cicli

richiesta = int(input("Inserisci un numero: "))
recap = True

while recap:
    for i in range(richiesta, -1, -1):
        print(richiesta)
        richiesta -= 1
    
    scelta = input("Vuoi continuare? si o no: ")
    if scelta == "si":
        richiesta = int(input("Inserisci un nuovo numero "))
    else:
        recap= False
    


    
    
    

numero = int(input("Inserisci un numero: "))
n_primo= True
contatore = 0

while contatore < 5:
    for i in range(numero):
        if numero%2==0:
            print("Il numero è pari")    
        else:
            print("Il numero è dispari")
             
        if numero%i==0:
            n_primo=False
        
        else:
            n_primo=True
            print("Il numero è primo")
            contatore +=1
            
            

         

        
    