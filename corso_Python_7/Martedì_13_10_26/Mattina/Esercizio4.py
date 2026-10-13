# Classe base: rappresenta un prodotto generico
class Prodotto:

    # Costruttore: salva nome, costo di produzione e prezzo di vendita
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome                          # nome del prodotto
        self.costo_produzione = costo_produzione  # quanto costa produrlo
        self.prezzo_vendita = prezzo_vendita      # a quanto viene venduto

    # Metodo che calcola il profitto
    def calcola_profitto(self):
        print(f"Il profitto è di {self.costo_produzione - self.prezzo_vendita} euro")


# Classe Elettronica che EREDITA da Prodotto
class Elettronica(Prodotto):

    # Costruttore: aggiunge l'attributo "garanzia"
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)  # richiama il costruttore di Prodotto
        self.garanzia = garanzia  # attributo specifico: durata della garanzia

    # Metodo specifico: mostra la garanzia
    def visualizza_garanzia(self):
        print(f"La tua garanzia è di {self.garanzia} anni")


# Classe Abbigliamento che EREDITA da Prodotto
class Abbigliamento(Prodotto):

    # Costruttore: aggiunge l'attributo "materiale"
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)  # richiama il costruttore di Prodotto
        self.materiale = materiale  # attributo specifico: tipo di tessuto

    # Metodo specifico: mostra il materiale usato
    def visualizza_materiale(self):
        print(f"Il materiale usato per questo capo è {self.materiale}")


# --- Creazione delle istanze ---

Product = Prodotto("Generico", 0, 0)                    # istanza della classe base
Elettr = Elettronica("IPhone 18 PRO", 1880, 1600, "5 Anni")  # istanza di Elettronica
Elettr.visualizza_garanzia()  # → "La tua garanzia è di 5 Anni anni"
Elettr.calcola_profitto()     # → "Il profitto è di 280 euro"
print("----------------------------------------")  # separatore visuale

Moda = Abbigliamento("Felpa Adidas", 45, 30, "Cotone")  # istanza di Abbigliamento
Moda.visualizza_materiale()  # → "Il materiale usato per questo capo è Cotone"
Moda.calcola_profitto()      # → "Il profitto è di 15 euro"

print("------------EXTRA--------------")

class Fabbrica():   #classe che rappresenta una fabbrica con un inventario
    

    def __init__(self, prodotto):
        self.prodotto = prodotto
        self.inventario = {}  #dizionario per memorizzare nome -> quantita

    def aggiungi_prodotto(self, nome, quantita):    #aggiunge un prodotto all'inventario
        
        if nome in self.inventario:
            self.inventario[nome] += quantita  #somma alla quantita esistente
        else:
            self.inventario[nome] = quantita   #crea la voce con la quantita data

    def vendi_prodotto(self, nome, quantita, prezzo):   #vende un prodotto: controlla stock e sottrae dall'inventario
        
        if nome not in self.inventario:
            print("Prodotto non disponibile!")  #blocco se non c'è 
        self.inventario[nome] -= quantita       #riduce lo stock
        print(f"Il profitto della vendita è di {quantita * prezzo} euro")  #mostra il guadagno

    def resi_prodotto(self, nome, quantita): #gestisce un reso: aumenta la quantita del prodotto nell'inventario
        
        if nome in self.inventario:
            self.inventario[nome] += quantita   #somma il reso allo stock esistente
        else:
            self.inventario[nome] = quantita    #crea la voce se il prodotto non c'era


print("-----------------------MENU'------------------------")  
Fabric = Fabbrica(0)  #crea l'istanza della fabbrica
scelta = int(input("Cosa vuoi fare: 1 aggiungere un prodotto, 2 vendere un prodotto, 3 dare il reso di un prodotto"))  

while scelta != 0:  #loop finche l'utente non inserisce 0

    if scelta == 1:
        nome = input("Nome prodotto: ")  #chiede il nome del prodotto
        quantita = int(input("Quantità: "))  #chiede la quantita da aggiungere
        Fabric.aggiungi_prodotto(nome, quantita)  #chiama il metodo di aggiunta

    elif scelta == 2:
        nome = input("Nome prodotto: ")  #chiede quale prodotto vendere
        quantita = int(input("Quantità: "))  #chiede quante unita vendere
        prezzo = int(input("Che prezzo fa il prodotto selezionato? "))  #chiede il prezzo unitario
        Fabric.vendi_prodotto(nome, quantita, prezzo)  #chiama il metodo di vendita

    elif scelta == 3:
        nome = input("Nome prodotto: ")  #chiede quale prodotto restituire
        quantita = int(input("Quanti capi vuoi restituire? "))  #chiede la quantita del reso
        Fabric.resi_prodotto(nome, quantita)  #chiama il metodo di reso

    else:
        print("Scelta errata")  #messaggio per input non validi

    scelta = int(input("Cosa vuoi fare: 1 aggiungere un prodotto, 2 vendere un prodotto, 3 dare il reso di un prodotto"))  
        
    
        
        
    
    


    