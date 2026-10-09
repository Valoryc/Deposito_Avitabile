import utility as u

scelta=int(input("Che operazione vuoi fare? 1 somma , 2 sottrazione, 3 moltiplicazione , 4 divisione e 0 per uscire: "))

while scelta != 0:
    
        if scelta == 1:
            n1=int(input("Inserisci il primo numero: "))
            n2=int(input("Inserisci il secondo numero: "))
            u.somma(n1,n2)
            
        elif scelta == 2:
            n1=int(input("Inserisci il primo numero: "))
            n2=int(input("Inserisci il secondo numero: "))
            u.sottrazione(n1,n2)
            
        elif scelta == 3:
            n1=int(input("Inserisci il primo numero: "))
            n2=int(input("Inserisci il secondo numero: "))
            u.moltiplicazione(n1,n2)
        
        elif scelta == 4:
            n1=int(input("Inserisci il primo numero: "))
            n2=int(input("Inserisci il secondo numero: "))
            if n2 == 0:
                print("Non puoi fare la divisione")
            else:
                u.divisione(n1,n2)
        
        else:
            print("Scelta sbagliata")
        scelta=int(input("Che operazione vuoi fare? 1 somma , 2 sottrazione, 3 moltiplicazione , 4 divisione e 0 per uscire: "))
        
        