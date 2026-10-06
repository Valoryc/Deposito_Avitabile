#Esercizi con i Match

#Inserimento dell'utente sulla propria età
eta = input("La tua età è maggiore o uguale a 18?: ")

#Capire se l'età è consona alla visione del film
match eta:
    case "si":
        print("Puoi guardare il film")
        
    case "no":
        print("Non puoi guardare il film") 
        
        
        
    
#Inserimento dei due numeri        
num1 = int(input("Inserisci il primo numero "))
num2 = int(input("Inserisci il secondo numero "))

#Piccolo menu per le operazioni
scelta = input("Quale operazione vuoi fare? Addizione, Sottrazione, Moltiplicazione, Divisione ")
  
#Tutte le operazioni con i medesimi risultati      
match scelta:
    
    case "addizione":
        print("Il risultato dell'addizione è: ", num1 + num2 )
        
    case "sottrazione":
        print("Il risultato della sottrazione è: ", num1 - num2)
        
    case "moltiplicazione": 
        print("Il risultato della moltiplicazione è: " , num1 * num2)
        
    case "divisione":
        if num2 == 0:
            print("Impossibile effettuare l'operazione")
        
        else:
            print("Il risultato della divisione è: " , num1 / num2)
    
    case _:
        print("Scelta invalida")   
        
        
        
        

#Creazione della lista con i suoi elementi
nome=input("Inserisci nome: ")
eta = int(input("Inserisci età: "))
sesso = input("Inserisci il sesso: ")
premium= bool(input("Sei premium? "))

lista = [nome , eta , sesso , premium]

print(lista)

#Menu per le operazioni da fare sulla lista
print("----------------------------------------------------------")
print("Vuoi modificare qualcosa all'interno della tua lista?")
scelta = input("Inserisci una di queste opzioni: Nome, Eta, Sesso, Premium, Rimozione ,Creare Lista: ")
print("----------------------------------------------------------")
match scelta:
    
    case "nome":
        nome2 = input("Inserisci il nuovo nome: ")
        lista[0] = nome2
        print(lista)

    case "eta":
        eta2 = int(input("Inserisci la nuova età: "))
        lista[1] = eta2
        print(lista)

    case "sesso":
        sesso2 = input("Inserisci il nuovo sesso: ")
        if len(sesso2) > 1:
            print("Sei scemo, riinserisci")
            sesso2 = input("Inserisci il sesso con un solo carattere: ")
        lista[2] = sesso2
        print(lista)

    case "premium":
        premium2 = bool(input("Sei premium? true/false: "))
        lista[3] = premium2 
        print(lista)

    case "rimozione":
        scelta=input("Cosa vuoi rimuovere? Nome, Eta , Sesso o Premium? ")
        if scelta == 'nome':
            lista.pop(0)
        
        elif scelta == 'eta':
            lista.pop(1)
            
        elif scelta == 'sesso':
            lista.pop(2)
        
        elif scelta == 'premium':
            lista.pop(3)    
        
        print(lista)
        
    case "lista2":
        
        nome3 =input("Inserisci nome: ")
        eta3 = int(input("Inserisci età: "))
        sesso3 = input("Inserisci il sesso: ")
        premium3 = bool(input("Sei premium? "))
        lista2 = [nome3 , eta3 , sesso3 , premium3]  
        
        print(lista2)  
    
    case _:
        print("Scelta invalida")

        
    
