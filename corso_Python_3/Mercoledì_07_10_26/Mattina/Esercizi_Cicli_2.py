#Esercizi con tutti i cicli

#Numeri pari o dispari tramite controllo if - else
numero=int(input("Inserisci un numero: "))

if numero%2==0:
    print("Il numero è pari")
else:                               #verifica pari o dispari
    print("Il numero è dispari") 
    
print("------------------------------------------------------------") 

#Ciclo booleano 
num=int(input("Inserisci un numero: "))
cap=True

while num < 0:
    num=int(input("Inserisci un altro numero: "))  #controllo se il numero è positivo o negativo
    
while cap:
    for i in range(num, -1, -1):
        print(num)
        num-=1                      #conto alla rovescia
        
    scelta=input("Vuoi ripetere? si/no ")
    if scelta.lower() == "no":      #scelta per ripetere o meno il ciclo
        cap=False
    else:
        num=int(input("Inserisci un altro numero: "))  #numero da inserire

print("------------------------------------------------------------") 

#Calcolo del quadrato degli elementi all'interno della lista popolata dall'utente
lunghezza=int(input("Inserisci la lunghezza della lista: "))
numeri= []

for i in range(lunghezza):
    numeri.append(int(input("Inserisci i numeri della tua lista: "))) #inserimento elementi all'interno della lista
    numeri[i]**=2
    
print(numeri) 

print("------------------------------------------------------------") 

#Creare una lista, verificare se è vuota, sennò il massimo fra i numeri inseriti e quanti numeri ci sono all'interno
grandezza = int(input("Inserisci la lunghezza della lista: "))

listaNu = []

for i in range(grandezza):
    listaNu.append(int(input("Inserisci i numeri nella lista: "))) #inserimento numeri nella lista
        
if len(listaNu) == 0:
    print("La lista è vuota")
else:                           #controllo lista, se è vuota o se è piena cerca il massimo
    massimo = listaNu[0]
    for i in range(grandezza):
        if listaNu[i]> massimo:
            massimo= listaNu[i]
        
    print("Il massimo è: ", massimo) 


while len(listaNu)>0:
    print("I numeri all'interno della lista sono: ", len(listaNu)) #stampa la lunghezza della lista
    break


    
    
    
