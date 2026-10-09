#Esercizio:  Andare a creare un sistema ripetibile che permetta di inserire: 
# sia al fondo che nella posizione che vogliamo noi, modificare, stampare ed eliminare liste, 
# che sono divise dal tipo che viene scelto.


lista = []
tipo=input("Vuoi una lista di numeri o di stringhe? ")


lunghezza=int(input("Inserisci la lunghezza della lista: "))

if tipo == "stringhe":
        
        for i in range(lunghezza):
            p=input("Inserisci la parola nella lista: ")
            lista.append(p)

        scelta=input("Quale operazione vuoi fare: 1 aggiungere al fondo, 2 aggiungere nella posizione scelta, 3 modificare, 4 stampare , 5 eliminare la lista? ")

        match scelta:
            case "1": 
                parolaFondo=input("Quale parola vorresti aggiungere alla fine? ")
                lista.append(parolaFondo)
                
            case "2":
                valore=input("Quale parola vorresti aggiungere? ")
                posizione=int(input("In quale posizione lo vuoi? "))
                
                lista.insert(posizione,valore)
                print(lista)
                
            case "3":
                posizione=int(input("In quale posizione vuoi modificare la parola? "))
                if posizione > 0:
                    valore=input("Inserisci una nuovo parola:  ")
                    lista[posizione] = valore
                
                print(lista)
                
            case "4":
                print("Lista ", lista)
                
            case "5":
                lista.clear()
                print("Lista vuota!")
                
elif tipo == "numeri":
        

        for i in range(lunghezza):
            n=int(input("Inserisci il numero nella lista: "))
            lista.append(n)

        scelta=input("Quale operazione vuoi fare: 1 aggiungere al fondo, 2 aggiungere nella posizione scelta, 3 modificare, 4 stampare , 5 eliminare la lista? ")

        match scelta:
            case "1": 
                numeroFondo=int(input("Quale numero vorresti aggiungere alla fine? "))
                lista.append(numeroFondo)
                
            case "2":
                valore=int(input("Quale valore vorresti aggiungere? "))
                posizione=int(input("In quale posizione lo vuoi? "))
                
                lista.insert(posizione,valore)
                print(lista)
                
            case "3":
                posizione=int(input("In quale posizione vuoi modificare il numero? "))
                if posizione > 0:
                    valore=int(input("Inserisci un nuovo valore:  "))
                    lista[posizione] = valore
                
                print(lista)
                
            case "4":
                print("Lista ", lista)
                
            case "5":
                lista.clear()
                print("Lista vuota!")
                
else:
        print("scelta sbagliata!!")
        
        
    
    