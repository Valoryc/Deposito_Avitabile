#Esercizi pomeriggio

def richiesta(num):

    while num <= 0:
        print("Inserisci un numero valido: ")   #Funzione creata per controllare se il numero inserito è valido o meno
        num=int(input(" "))
    return num
        
def numeroPrimo(num):
    for i in range(2,num):
        if num%i == 0:          #Funzione creata per dirci se il numero è primo o no
             return False
    return True


somma=0
scelta=int(input("Che esercizio vuoi fare? 1, 2, 3, 4, 5: "))       #menu di scelta delle opzioni
while scelta > 0:
    if scelta == 1:

        num=int(input("Inserisci un numero: "))
        richiesta(num)
        lista=[* range(num)]            #creazione della lista grazie al numero inserito dall'utente e verifica se il numero è primo o meno
        print(lista)
        print("Il numero è primo? ",numeroPrimo(num))
    
    elif scelta == 2:
        for i in range(1,num):
                                    #somma dei numeri pari all'interno della lista
            if i%2==0:
                somma+=i
                
                
        print("La somma dei pari è: ", somma)

        print("-----------------------------------")

    elif scelta == 3:
        print("Stampa numeri Dispari")
        for i in range(1, num):             #stampa tutti i numeri dispari all'interno della lista
            
            if i%2==1:
                print(i)
                
        print("------------------------------------")

    elif scelta == 4:
        print("Stampa numeri primi nella lista")
        for i in range(num):                        #stampa tutti i numeri primi della lista
            if i >= 2 and numeroPrimo(i):
                print(i)


        print("------------------------------------")
    
    elif scelta == 5:
        print("Stampa della somma totale dei numeri e verifica se è primo o meno")
        sommaFinale = 0
        for i in range (1, num):
            sommaFinale+=i
            
                                                                                #stampa la somma totale di tutti i numeri nella lista
        if sommaFinale >=2 and numeroPrimo(sommaFinale):                        #e verifichiamo se il numero totale è primo o no
            print("La somma: " , sommaFinale , " è un numero primo")

        else:
            print("La somma: " , sommaFinale , " non è un numero primo")
            
        
    else:
        print("Scelta sbagliata riprova")
        
    scelta=int(input("Inserisci una scelta da 1 a 5, o per uscire 0: "))        #scelta se vuole provare con un altra opzione o meno