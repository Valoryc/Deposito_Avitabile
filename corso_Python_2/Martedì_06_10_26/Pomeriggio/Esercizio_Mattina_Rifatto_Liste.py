#Esercizio Mattina rifatto

lista1 = [1,2,3,4,5]

lista2 = ["Valeria", "Giulia", "Francesca", "Marta", "Chiara"]

scelta = int(input("Scegli tra 1 e 2: "))

if scelta == 1:
    s1= input("Vuoi aggiungere un numero alla lista1? (si/no): ")
    if s1 == "si":
        elemento = int(input("Inserisci il numero da aggiungere: "))
        lista1.append(elemento)
    
    elif s1 == "no":
        print("Nessun numero aggiunto alla lista1.")
        
        
    s2 = input("Vuoi rimuovere un numero dalla lista1? (si/no): ")
    if s2 == "si":
        elemento = int(input("Inserisci il numero da rimuovere: "))
        lista1.remove(elemento)
    
    elif s2 == "no":
        print("Nessun numero rimosso dalla lista1.")

    print("Lista1:", lista1)

elif scelta == 2:
    s3 = input("Vuoi aggiungere una parola alla lista2? (si/no): ")
    if s3 == "si":
        elemento = input("Inserisci la parola da aggiungere: ")
        lista2.append(elemento)
        
    elif s3 == "no":
        print("Nessuna parola aggiunta alla lista2.")
    
    
    s4 = input("Vuoi rimuovere una parola dalla lista2? (si/no): ")
    if s4 == "si":
        elemento = input("Inserisci la parola da rimuovere: ")
        lista2.remove(elemento) 
    
    elif s4 == "no":
        print("Nessuna parola rimosso dalla lista2.")
        
    
    print("Lista2:", lista2)
    

else:
    print("Scelta non valida")