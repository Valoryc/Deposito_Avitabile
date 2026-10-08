#Esercizi Funzioni

from random import randint  #importo della libreria random


def random():                   
    return randint(1,100)   #funzione per la generazione di numeri casuali
    

x=random()   
numeroUtente=int(input("Che numero vuoi pensi sia quello corretto? "))  #inserimento da parte dell'utente

while numeroUtente != 0:        #ciclo while per ripetere nel caso in cui abbia sbagliato o voglia uscire dal gioco
    
    if numeroUtente > x:
        print("Il numero è maggiore di quello corretto")
    elif numeroUtente < x:
        print("Il numero è minore di quello corretto")      #Verifica del numero se è più altro o più basso del numero da indovinare
    else:
        print("Hai indovinato!!")
        
    numeroUtente=int(input("Inserisci di nuovo un numero o premi 0 per uscire "))   #Messaggio di inserimento di un nuovo numero o se vuole uscire
    
    
def fibonacci(n):
    if n<=1:            #Funzione per il calcolo di Fibonacci
        return n
    return fibonacci(n-1)+fibonacci(n-2)

n = int(input("Inserisci un numero: "))     #Richiesta del numero dall'utente
i = 0       #stabiliamo un indice di partenza
while fibonacci(i) <= n:
    print(fibonacci(i)) #ciclo while che ci aiuta con la stampa della sequenza fino a quando la condizione non è soddisfatta
    i += 1  #incremento dell'indice ogni volta che la condizione è conclusa





    
    
