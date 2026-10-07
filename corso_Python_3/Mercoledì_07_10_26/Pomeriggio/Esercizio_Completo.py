#Esercizio completo

richiestaNumero=int(input("Inserisci un numero: "))
somma=0


while richiestaNumero<=0:
    print("Numero sbagliato, inserisci di nuovo: ")
    richiestaNumero=int(input(" "))
    
risultatoFinale = []
risultatoFinale.append(richiestaNumero)

for i in range(1,richiestaNumero):
    
    if i%2==0:
        somma+=i
        
risultatoFinale.append(somma)


dispari = []
for i in range(1, richiestaNumero):
    
    if i%2==1:
        dispari.append(i)

risultatoFinale.append(dispari)
        
n_primo=True
for i in range(2, richiestaNumero):

    if richiestaNumero % i ==0:
        n_primo=False
        break

risultatoFinale.append(n_primo)

if n_primo and richiestaNumero > 1:
    print("Il numero è primo")
else:
    print("Il numero non è primo")
    

print(risultatoFinale)