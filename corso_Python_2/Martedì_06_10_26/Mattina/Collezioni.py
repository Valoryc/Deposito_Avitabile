#Esercizio con Collezioni (Liste)

numero=[1,2,3,4,5,6,7,8,9,10]
#sostituzione di alcuni elementi della lista
numero[9]=100 
numero[8]=20
numero[4]=10  

print(numero)

print("-----------------------------------------")

persone=["Giovanni", "Paolo", "Maria"]

mix=[1, "ciao", 3.14, False]

#stampa del sesto e del terzo elemento all'interno della lista
print(numero[6])
print(numero[3])

print("-----------------------------------------")

print(persone[0])

print("-----------------------------------------")

#prova di tutti i metodi delle liste
print(len(numero))

print("-----------------------------------------")

numero.append(230) #aggiunge un elemento alla fine 
print(numero)

print("-----------------------------------------")

numero.insert(4, 1) #inserisce un elemento alla posizione indicata
print(numero)

print("-----------------------------------------")

numero.remove(20) #rimuove il valore
print(numero)

print("-----------------------------------------")

numero.sort() #ordina la lista
print(numero)

print("-----------------------------------------")

num= numero[4] #stampiamo il valore nella medesima posizione
print (num)

print("-----------------------------------------")

numero.clear() #svuota la lista