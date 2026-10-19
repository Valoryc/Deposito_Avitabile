def creazione_file():
    
    nome= input("Come vuoi chiamare il tuo file? ")
    File= open(nome, "w")            #Metodo per creare il file con inserimento
    print("Hai creato il file!")
    
    inserimento=input("Cosa vuoi inserire nel file? ")
    File.write(inserimento)

    File.close()

def modifica_file():
    
    
    nome=input("Quale file vuoi modificare? ")
    File= open (nome, "w")               #Metodo per modificare il contenuto del file
    scrivere= input("Inserisci la tua modifica: ")
    File.write(scrivere)
    
    File.close()

def lettura_file():
    
    nome=input("Quale file vuoi leggere? ")
    File= open (nome, "r")       #Metodo per la lettura del contenuto del file
    contenuto=File.read()
    
    print(contenuto)
    File.close()
    
def cancellare_file():
    
    nome=input("Quale file vuoi cancellare? ")
    File= open (nome, "w")  
      
    print("Hai svuotato il file")       #Metodo per cancellare il contenuto del file
    File.write(" ")
    
    File.close()

    
print("----------------MENU----------------")

scelta = int(input("Cosa vuoi fare? 1 crea file, 2 modifica il file, 3 leggi il file, 4 cancella il file, 0 esci: "))

while scelta != 0:
    
    if scelta == 1:
        creazione_file()
        
    elif scelta == 2:
        modifica_file()
                                #Menu di scelta per l'utente, in base a quello che vuole fare all'interno del programma 
    elif scelta == 3:
        lettura_file()
        
    elif scelta == 4:
        cancellare_file()
        
    else:
        print("Scelta errata")
        
    scelta = int(input("Cosa vuoi fare? 1 crea file, 2 modifica il file, 3 leggi il file, 4 cancella il file, 0 esci: "))   #riscelta