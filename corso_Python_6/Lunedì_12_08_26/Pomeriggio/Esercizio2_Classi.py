class Garage:   #Definizione della classe Garage
                

    def __init__(self, capienza): #Metodo costruttore: inizializza un nuovo oggetto Garage
        
        self.capienza = capienza    #Assegna alla variabile d'istanza capienza il valore passato come parametro
        
        
        self.auto_presenti = []     #Inizializza una lista vuota che conterrà le targhe delle auto attualmente in garage
        

    def parcheggia(self, targa):    #Metodo per aggiungere un'auto al garage
        
        if targa in self.auto_presenti:  #Controlla se la targa è già presente nella lista delle auto
           
            print("L'auto e' gia' in garage")   #Stampa un messaggio di errore se l'auto è già presente
            
        elif len(self.auto_presenti) >= self.capienza:  #Controlla se il numero di auto è uguale o superiore alla capacità massima
            
            print("Garage pieno")   #Stampa messaggio se il garage è pieno
            
            
        else:       #Se nessuna delle condizioni precedenti è vera (auto non presente e garage non pieno)   
            
            self.auto_presenti.append(targa)    #Aggiunge la nuova targa alla lista
            print("Auto parcheggiata")  #Stampa conferma del parcheggio
            
            
    def rimuovi(self, targa):   #Metodo per rimuovere un'auto dal garage
        
        
        if targa in self.auto_presenti: #Controlla se la targa è presente nella lista
            
            self.auto_presenti.remove(targa)    #Rimuove la targa dalla lista
            
            print("Auto rimossa")   #Stampa conferma della rimozione

        else:    #Se la targa non è presente nella lista
              
            print("Errore: targa non presente") #Stampa messaggio di errore
            

    @staticmethod
    def formato_targa_valido(targa):    #Metodo statico per verificare il formato della targa
        
        if targa.isdigit() or targa.isalpha():   #Controlla se la targa è composta SOLO da numeri (isdigit) O SOLO da lettere (isalpha)
            
            print("Targa Non Italiana")  #Stampa messaggio se il formato è considerato non italiano
           
            
    def posti_liberi(self): #Metodo per calcolare i posti disponibili
        
        return self.capienza - len(self.auto_presenti)  #Restituisce la differenza tra la capacità totale e il numero di auto attualmente parcheggiate
        



Veicoli = Garage(10)    #Creazione di un'istanza della classe Garage con capacità di 10 auto


scelta = int(input("1 parcheggiare, 2 rimuovere, 3 posti liberi, 0 uscire: "))  #Richiesta iniziale della scelta all'utente e conversione in intero


while scelta != 0:  #Ciclo while che continua finché l'utente non sceglie 0 (uscire)
    
    if scelta == 1: #Se l'utente sceglie 1, parcheggia un'auto
        
        Veicoli.parcheggia(input("Inserisci la targa: ")) #Legge la targa da input e chiama il metodo parcheggia
        
    elif scelta == 2:    #Se l'utente sceglie 2, rimuove un'auto
        
        Veicoli.rimuovi(input("Targa da rimuovere: "))   #Legge la targa da input e chiama il metodo rimuovi
        
    elif scelta == 3:   #Se l'utente sceglie 3, visualizza i posti liberi
        
        print("Posti liberi:", Veicoli.posti_liberi())   #Stampa il numero di posti liberi calcolato dal metodo
       
    elif scelta == 4:   #Se l'utente sceglie 4, verifica il formato della targa
        
        targa = input("Inserisci la targa da verificare: ") #Legge la targa da input
        
        Valido = Veicoli.formato_targa_valido(targa)     #Chiede di verificare la targa. Nota: il risultato viene assegnato a Valido
    
    
    scelta = int(input("1 parcheggiare, 2 rimuovere, 3 posti liberi, 0 uscire: "))  #Aggiorna la scelta per il prossimo ciclo