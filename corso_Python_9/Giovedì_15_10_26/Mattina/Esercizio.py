class Fabbrica(): #classe Padre
    
    _registro=[]    #Variabile Protetta
    
    def __init__(self):     #costruttore con variabile protetta dentro della classe Fabbrica
        self._registro=[]   

    def riepilogo(self):        #Metodo ovveride della classe padre
        return "Fabbrica generica"
        
class Prodotto(Fabbrica):   #classe Figlia
    
    
    def __init__(self, prodotto, quantita): #costruttore di Prodotto
        super().__init__()      #richiama il costruttore della classe padre
        
        self.__nome_prodotto = prodotto #Incapsulamento: attributi privati
        self.__quantita_prodotto = quantita

    
    def get_nome(self):                 #Metodi per accedere ai dati privati (getter/setter)
        return self.__nome_prodotto

    def get_quantita(self):
        return self.__quantita_prodotto

    def set_quantita(self, nuova_quantita):
        if isinstance(nuova_quantita, int) and nuova_quantita >= 0:          #Verifico che il dato sia un numero intero e che sia maggiore o uguale a 0
            self.__quantita_prodotto = nuova_quantita
        else:
            print("Quantità non valida")

    def riepilogo(self):          
        return f"Prodotto: {self.get_nome()} | Quantità: {self.get_quantita()}" #Ovveride del metodo riepilogo della classe padre

class Gestione_Operazioni(Fabbrica): #CLASSE USATA PER LE OPERAZIONI (Figlia di Fabbrica)
    
    def __init__(self): #costruttore
        super().__init__() #richiama il costruttore della classe padre
        
    def aggiungi_prodotto(self):
        scelta1=input("Vuoi aggiungere un prodotto? ")
        if scelta1 == "si" or scelta1=="Si":
            prodotto=input("Inserisci il nome del prodotto: ")
            quantita=int(input("Inserisci la quantità del prodotto: "))     #Metodo nella quale andiamo ad aggiungere prodotti e quantita nella lista registro
            self._registro.append(prodotto)
            self._registro.append(quantita)
        else:
            print("Sei un pippo")

    def visualizza_produzione(self):
        scelta1=input("Vuoi visualizzare il registro produzione? ")
        if scelta1 == "si" or scelta1=="Si":            #Metodo per visualizzare la lista, con richiesta in caso di scelta fatta per sbaglio
            print(self._registro)
        else:
            print("Sei un pippo")
            
    def cerca_prodotto(self):
        ricerca=input("Quale prodotto vuoi cercare? ")
        for i in range(0, len(self._registro), 2):      #Metodo per ricercare il prodotto all'interno della lista
            if ricerca == self._registro[i]:
                print("Prodotto trovato")
                return
        print("Prodotto non trovato")
        
    def modifica_quantita(self):
        domanda=input("Vuoi modificare la quantità? ")
        if domanda == "si" or domanda=="Si":
            prodotto = input("Quale prodotto vuoi modificare? ")
            for i in range(0, len(self._registro), 2):              #Metodo per modificare la quantita con un for in un if
                if prodotto == self._registro[i]:
                    nuova_quantita = int(input("Inserisci la nuova quantità: "))
                    self._registro[i + 1] = nuova_quantita #i+1 posizione successiva 
                    print("Quantità aggiornata")
                    return
            print("Prodotto non trovato")
            
    def rimuovi_prodotto(self):
        domanda=input("Vuoi eliminare un prodotto? ")
        if domanda == "si" or domanda=="Si":
            prodotto = input("Quale prodotto vuoi eliminare? ")
            for i in range(0, len(self._registro), 2):      #Metodo per rimozione del prodotto all'interno della lista
                if prodotto == self._registro[i]:
                    self._registro.remove(prodotto)
                    print("Prodotto eliminato")
                    return
            print("Prodotto non trovato")
            
    def calcola_pezzi_totali(self):
        totale = 0
        for i in range(1, len(self._registro), 2):
            totale += self._registro[i]                     #Metodo che calcola i pezzi totali prodotti all'interno della lista
        print(f"Totale pezzi prodotti: {totale}")
        return totale

    def riepilogo(self):          
        return f"Gestione operazioni | Registro: {self._registro}"      #Metodo ovveride della classe padre


Gestione=Gestione_Operazioni() #richiamo della classe gestione_operazioni con un oggetto

print("------------MENU------------")
print("BENVENUTO SCEGLI LA TUA OPERAZIONE!")            #Menu
scelta = int(input("1 aggiungi prodotto, 2 Visualizza produzione, 3 Cerca prodotto, 4 Modifica quantità, 5 Rimuovi prodotto, 6 Calcola totale pezzi prodotti, 7 Esci "))

while scelta >= 1 and scelta < 7:
        
        if scelta == 1:
            Gestione.aggiungi_prodotto()
            print("------------------------------")
        
        elif scelta == 2:
            Gestione.visualizza_produzione()
            print("------------------------------")
            
        elif scelta == 3:
            Gestione.cerca_prodotto()           #If con scelta per le singole operazioni contenute all'interno della classe Gestione Operazioni
            print("------------------------------")
        
        elif scelta == 4:
            Gestione.modifica_quantita()
            print("------------------------------")
        
        elif scelta == 5:
            Gestione.rimuovi_prodotto()
            print("------------------------------")
        
        elif scelta == 6:
            Gestione.calcola_pezzi_totali()
            print("------------------------------")
        
        else:
            print("pippo")
            
        scelta = int(input("1 aggiungi prodotto, 2 Visualizza produzione, 3 Cerca prodotto, 4 Modifica quantità, 5 Rimuovi prodotto, 6 Calcola totale pezzi prodotti, 7 Esci "))
        #Riproposta di scelta