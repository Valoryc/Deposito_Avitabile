class MetodoPagamento:  # classe base
    def effettua_pagamento(self, importo):
        pass 

class CartaDiCredito(MetodoPagamento):  #erede di MetodoPagamento
    def effettua_pagamento(self, importo):  #sovrascrive il metodo della base
        print(f"Hai effettuato un pagamento con carta di {importo} euro")

class Paypal(MetodoPagamento):  #erede di MetodoPagamento
    def effettua_pagamento(self, importo):  #sovrascrive il metodo della base
        print(f"Hai effettuato un pagamento con PayPal di {importo} euro")

class BonificoBancario(MetodoPagamento):  #erede di MetodoPagamento
    def effettua_pagamento(self, importo):  #sovrascrive il metodo della base
        print(f"Hai effettuato un pagamento con Bonifico Bancario di {importo} euro")

class GestorePagamenti:  
    def __init__(self, method):
        self.method = method  #salva l'oggetto passato 

    def process(self, importo):
        self.method.effettua_pagamento(importo)  #POLIMORFISMO: la classe concreta decide cosa fare


def scegli_metodo():  # funzione che mostra le opzioni e restituisce un GestorePagamenti
    print("1 - Carta di credito")       # mostra la prima opzione
    print("2 - PayPal")                 # mostra la seconda opzione
    print("3 - Bonifico bancario")      # mostra la terza opzione
    scelta = int(input("Opzione (1/2/3): "))  # legge il numero inserito dall'utente
    if scelta == 1:                     # se ha scelto 1
        return GestorePagamenti(CartaDiCredito())  # crea e restituisce il gestore con carta
    elif scelta == 2:                   # se ha scelto 2
        return GestorePagamenti(Paypal())  # crea e restituisce il gestore con PayPal
    else:                               # se ha scelto 3 (o qualsiasi altro numero)
        return GestorePagamenti(BonificoBancario())  # crea e restituisce il gestore con bonifico


print("Scegli il metodo iniziale:")
gestore = scegli_metodo()  # crea il gestore con il metodo scelto

scelta = int(input("Vuoi 1 pagare, 2 cambiare metodo? (0 per uscire): "))  # prima lettura

while scelta != 0:  # ciclo finché non esce

    if scelta == 1:  # pagare
        importo = float(input("Inserisci l'importo da pagare: "))
        if importo <= 0:
            print("Importo invalido")
        else:
            gestore.process(importo)  # il gestore chiama il metodo della classe concreta

    elif scelta == 2:  # cambiare metodo
        gestore = scegli_metodo()  # nuovo gestore con il nuovo metodo

    else:  # numero non valido
        print("Errore di scelta")

    scelta = int(input("Vuoi 1 pagare, 2 cambiare metodo? (0 per uscire): "))  # prossima iterazione