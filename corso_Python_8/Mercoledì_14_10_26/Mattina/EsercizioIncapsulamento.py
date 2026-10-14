class ContoCorrente: #Definizione della classe che rappresenta un conto corrente

    __titolare = " "
    __saldo = 1         #attributi privati

    
    def __init__(self):    #Metodo costruttore
        self.__titolare = "Pippo"          #attributo privato: nome del titolare
        self.__saldo = 50000                #attributo privato: saldo attuale

    
    def get_titolare(self):
        return self.__titolare
                                        #metodi get e set del titolare
    def set_titolare(self, titolare):
        self.__titolare=titolare
        
    def get_saldo(self):
        return self.__saldo
                                        #metodi get e set del saldo
    def set_saldo(self, saldo):
        self.__saldo=saldo
    
    
    
    def deposita(self, importo): #Metodo per depositare (aggiungere) denaro al conto
        cambio_saldo=int(input("Inserisci il saldo da depositare: "))
        self.set_saldo(cambio_saldo)
        if cambio_saldo > 0:
                cambio_saldo += importo              #somma l'importo al saldo attuale
        else:
            print("Saldo Insufficiente")
    
    def preleva(self, importo):  #Metodo per prelevare (sottrarre) denaro dal conto
        cambio_saldo=int(input("Inserisci il saldo da depositare: "))
        self.set_saldo(cambio_saldo)
        if importo < cambio_saldo:
            print("Fondi insufficienti")   #blocca il prelievo se non ci sono fondi sufficienti
        else:
            cambio_saldo -= importo          #sottrae l'importo dal saldo

    
    def visita_contocorrente(self):     #Metodo che restituisce un messaggio con i dati del conto
        return f"Il saldo di {self.__titolare} è di: {self.__saldo} euro"



print("-------------------------MENU----------------------------")
Conto = ContoCorrente() #Crea un'istanza della classe ContoCorrente con saldo iniziale 0


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