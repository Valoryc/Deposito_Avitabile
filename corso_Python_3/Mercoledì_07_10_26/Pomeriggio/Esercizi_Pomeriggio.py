#Esercizi Pomeriggio sui Cicli

scelta=int(input("Quale esercizio vuoi fare? Lista-1, scomponi parola-2, o massimo numeri-3: "))

while scelta > 0:
    if scelta == 1: 
        lunghezza= int(input("Inserisci la lunghezza della lista: "))
        listaNumeri= []
        somma = 0
        temp= 0

        for i in range(lunghezza):
            listaNumeri.append(int(input("Inserisci numero: "))) #Inserimento dei numeri all'interno della lista
            
            if listaNumeri[i]==0:
                temp=0              #confronto a 0, conseguenza del while
                
                while temp < i:
                    somma+=listaNumeri[temp]        #temp < i sommerà tutti gli elementi all'interno della lista fino a quando non è 0 che interromperà tutto
                    temp+=1
                break
            
        print(somma) 
    

    elif scelta == 2:
        parola=input("Inserisci una parola: ")

        for i in range(len(parola)):        #calcolo lunghezza parola e poi stampa delle singole lettere
            print(parola[i])
           
         
    elif scelta == 3:        
        max=int(input("Fino a quale numero vuoi arrivare? "))
        step=int(input("Quanti step vuoi fare? "))

        for i in range(0,max,step): #elenco numerico specificato dall'utente
         print(i) 
        
    else:
        print("Scelta errata")
    
    scelta=int(input("Inserisci una nuova scelta (0 per uscire)")) #elenco dinamico
        
    
