#Esercizio:  Andare a creare un sistema ripetibile che obblighi l'utente a inserire nome e codice, 
# poi l'utente può accedere ad un secondo pezzo del menu, 
# solo se ha inserito i dati nella fase prima e dopo un login (codice == codice e nome == nome) questa seconda parte deve permettere di visionare due operazioni,
# somme e sottrazioni e salvare ogni risultato di ogni operazione, entrambi i menu ripetibili ( menu: registrazione // login --> dentro login: 
# le due operazioni e visualizza risultati)

nomePrefix="Valentina"
codicePrefix=33
listaRisultati= []

print("BENVENUTO, FAI L'ACCESSO!")

while True:
    nome=input("Inserisci il tuo nome: ")
    codice=int(input("Inserisci il tuo codice: "))
    
    if codice == codicePrefix and nome == nomePrefix:
        scelta=int(input("Inserisci la scelta che vuoi fare: 1 per la somma e 2 per la sottrazione "))
        if scelta == 1:
            somma=0
            n1=int(input("Inserisci il primo numero: "))
            n2=int(input("Inserisci il secondo numero: "))
            
            somma=n1+n2
            listaRisultati.append(somma)
            
        
        elif scelta ==2:
            sottrazione=0
            
            n1=int(input("Inserisci il primo numero: "))
            n2=int(input("Inserisci il secondo numero: "))
            
            sottrazione=n1-n2
            listaRisultati.append(sottrazione)
            
            
        else:
            print("Hai sbagliato")
    
    else: 
        print("Inserisci i dati da capo!!!!")
        break
    
    
    print(listaRisultati)