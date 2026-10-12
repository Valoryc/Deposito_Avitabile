class ContoCorrente: #Definizione della classe che rappresenta un conto corrente

    
    def __init__(self, intestatario, saldo):    #Metodo costruttore
        self.intestatario = intestatario   #attributo: nome del titolare
        self.saldo = saldo                 #attributo: saldo attuale

    
    def deposita(self, importo):            #Metodo per depositare (aggiungere) denaro al conto
        self.saldo += importo              #somma l'importo al saldo attuale

    
    def preleva(self, importo):             #Metodo per prelevare (sottrarre) denaro dal conto
        if importo > self.saldo:
            print("Fondi insufficienti")   #blocca il prelievo se non ci sono fondi sufficienti
        else:
            self.saldo -= importo          #sottrae l'importo dal saldo

    
    def visita_contocorrente(self):     #Metodo che restituisce un messaggio con i dati del conto
        return f"Il saldo di {self.intestatario} è di: {self.saldo} euro"



print("-------------------------MENU----------------------------")


intestatario = input("BENVENUTO INSERISCI IL TUO NOME: ") #Chiede all'utente il nome dell'intestatario


Conto = ContoCorrente(intestatario, 0) #Crea un'istanza della classe ContoCorrente con saldo iniziale 0


scelta = int(input("Vuoi 1 depositare, 2 prelevare o 3 visualizzare? (0 per uscire): ")) #Chiede la prima scelta all'utente (convertita in intero)


while scelta != 0: #Ciclo che continua finché l'utente non sceglie 0 (uscita)

    if scelta == 1:
        importo = float(input("Inserisci il valore che vuoi depositare: "))
        if importo <= 0:
            print("Importo invalido")      #rifiuta importi negativi o zero
        else:
            Conto.deposita(importo)        #chiama il metodo deposita sull'oggetto

    elif scelta == 2:
        importo = float(input("Inserisci il tuo importo: "))
        Conto.preleva(importo)             #chiama il metodo preleva (con controllo interno)

    elif scelta == 3:
        print(Conto.visita_contocorrente())  #stampa i dati del conto
        
    else:
        print("Errore di scelta")           #numero inserito non tra 0, 1, 2, 3

    #Chiede la scelta successiva per la prossima iterazione del ciclo
    scelta = int(input("Vuoi 1 depositare, 2 prelevare o 3 visualizzare? (0 per uscire): "))   