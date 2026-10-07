#Esercizi Cicli

#ciclo booleano
richiesta = int(input("Inserisci un numero: "))
recap = True

while recap:
    for i in range(richiesta, -1, -1):      #dal ciclo for noi facciamo il conto alla rovescia fino a 0 (0 compreso)
        print(richiesta)
        richiesta -= 1
    
    scelta = input("Vuoi continuare? si o no: ") #si fa scegliere all'utente se vuole continuare o meno
    if scelta == "si":
        richiesta = int(input("Inserisci un nuovo numero ")) #nel caso fosse si, si rinserisce un numero
    else:
        recap= False 
    


print("------------------------------------------------------------")   
    
    

#Esercizio while con if integrati 
numero =int(input("Inserisci un numero: "))
contatore = 0
  

while contatore < 5:
    
    if numero%2==0:
        print("Il numero è pari")    
    else:                               #calcolo se il numero è pari o dispari
        print("Il numero è dispari")
      
    n_primo= True  #assegniamo variabile valore True per i num primi
       
    for i in range(2, numero):  
        if numero % i == 0: 
            n_primo = False
                            #controllo se il numero è primo oppure no
    if n_primo:
        print("Il numero è primo")
        contatore += 1
        
    numero =int(input("Inserisci un numero: ")) #inserimento da capo per i numeri che non sono primi
        
        
if contatore == 5:
    print("Hai inserito 5 numeri primi")

            
            

         

        
    