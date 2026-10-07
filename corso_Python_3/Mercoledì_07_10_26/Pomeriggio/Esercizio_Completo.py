#Esercizio completo

richiestaNumero=int(input("Inserisci un numero: "))
somma=0


while richiestaNumero<=0:
    print("Numero sbagliato, inserisci di nuovo: ")  #messaggio d'errore nell'inserimento 0 o 0<
    richiestaNumero=int(input(" "))
    
risultatoFinale = [] #creazione della lista che conterrà tutti gli elementi
risultatoFinale.append(richiestaNumero)

for i in range(1,richiestaNumero):
    
    if i%2==0:  #somma dei soli numeri pari
        somma+=i
        
risultatoFinale.append(somma)   #inseriamo il risultato finale della somma all'interno della lista finale


dispari = []    #creazione lista per la sequenza dei numeri dispari
for i in range(1, richiestaNumero):
    
    if i%2==1:
        dispari.append(i) #inserimento dei numeri dispari all'interno della lista dispari

risultatoFinale.append(dispari) #inserimento della lista dispari all'interno dell'ultima lista
        
n_primo=True
for i in range(2, richiestaNumero):

    if richiestaNumero % i ==0:
        n_primo=False       #verifica se il numero è primo oppure no
        break

risultatoFinale.append(n_primo) #inseriamo la verifica all'interno della lista finale

if n_primo and richiestaNumero > 1:
    print("Il numero è primo")
else:                                   #ulteriore verifica con stampa se è primo o meno
    print("Il numero non è primo")
    

print(risultatoFinale)      #stampa finale con tutti gli elementi