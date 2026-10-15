from abc import ABC, abstractmethod  # import per fare classi astratte

class VeicoloTrasporto(ABC):  # classe astratta base, non si può creare direttamente

    _targa=" "          # attributo di classe (default)
    _peso_massimo= 25000
    _carico_attuale= 0

    def __init__(self, __targa, __peso, __carico):
        self._targa= __targa
        self._peso_massimo=__peso
        self._carico_attuale=__carico

    def carico (self,__peso):  # aggiunge peso al veicolo
        if self._peso_massimo > __peso:
            print("Il peso supera la capacità")
        else:
            self._peso_massimo+=1
            return

    def scarica (self):  # svuota il carico
        self._carico_attuale = 0
        return

    @abstractmethod
    def costo_manutenzione(self):  # ogni classe figlia DEVE riscriverlo
        return 0


class Camion(VeicoloTrasporto):  # camion eredita da VeicoloTrasporto

    def __init__(self, __targa, __peso, __carico, numero_assi):
        super().__init__(__targa, __peso, __carico)  # chiamo il __init__ del genitore
        self.numero_assi=numero_assi

    
    def costo_manutenzione():  # costo = assi*100 + chili*1
        asse_domanda=int(input("Quanti assi hai? "))
        asse_domanda*=100
        
        chili_domanda=int(input("Quanti chili trasporti? "))
        chili_domanda*=1
        
        print("Il costo di manutenzione totale è di ", asse_domanda + chili_domanda , " euro")
        return asse_domanda + chili_domanda  # restituisco il numero per poterlo sommare


class Furgone(VeicoloTrasporto):  # furgone eredita da VeicoloTrasporto

    def __init__(self, __targa, __peso, __carico, alimentazione):
        super().__init__(__targa, __peso, __carico)
        self.alimentazione=alimentazione

    
    def costo_manutenzione():  # diesel=150, elettrico=200
        costo=150
        costo2=200
        
        scelta=(input("Hai la macchina diesel o elettrica?"))
        if scelta == "diesel":
            
            print("La tua manutenzione costa ", costo ," euro")
            return costo
        
        elif scelta == "elettrico":
            print("La tua manutenzione costa ", costo2 ," euro")
            return costo2
        return 0


class Motocarro(VeicoloTrasporto):  # motocarro eredita da VeicoloTrasporto

    def __init__(self, __targa, __peso, __carico):
        super().__init__(__targa, __peso, __carico)

    
    def costo_manutenzione():  # costo = anni*50
        anni_domanda=int(input("Quanti anni di servizio hai? "))
        anni_domanda*=50
        print("Il costo totale di manutenzione è di ", anni_domanda , " euro")
        return anni_domanda


class GestoreFlotta:  # classe che gestisce la lista di veicoli

    _veicoli=[]

    def __init__(self):
        self._veicoli=[]  # lista che conterrà gli oggetti veicolo

    def aggiungi_veicolo(self):  # aggiunge un veicolo alla lista
        scelta1=input("Vuoi aggiungere un veicolo? ")
        if scelta1 == "si" or scelta1=="Si":
            scelta2=input("Vuoi aggiungere un Camion, Furgone o Motocarro? ")
            if scelta2=="Camion":
                
                targa=input("Inserisci la targa del Camion ")
                peso=int(input("Peso massimo? "))
                carico=int(input("Carico attuale? "))
                assi=int(input("Quanti assi? "))
                self._veicoli.append(Camion(targa, peso, carico, assi))  # salvo l'oggetto, non la targa
                
            elif scelta2=="Furgone":
                
                targa2=input("Inserisci la targa del Furgone ")
                alimentazione=input("Diesel o elettrico? ")
                self._veicoli.append(Furgone(targa2, peso, carico, alimentazione))
                
            elif scelta2=="Motocarro":
                
                targa3=input("Inserisci la targa del Motocarro ")
                self._veicoli.append(Motocarro(targa3, peso, carico))
                
            else:
                print("Sei un doppio pippo")
        else:
            print("Sei un pippo")

    def rimuovi_veicolo(self):  # cerca per targa e toglie dalla lista
        domanda=input("Vuoi eliminare un veicolo? ")
        if domanda == "si" or domanda=="Si":
            targa_da_cercare = input("Quale targa vuoi eliminare? ")
            for i in range(0, len(self._veicoli)):
                if self._veicoli[i]._targa == targa_da_cercare:  # confronto la targa dell'oggetto
                    self._veicoli.pop(i)  # rimuovo l'oggetto in quella posizione
                    print("Veicolo eliminato")
                    return
            print("Veicolo non trovato")

    def costo_totale_manutenzione(self):  # somma il costo di TUTTI i veicoli nella lista
        totale = 0
        for veicolo in self._veicoli:  # giro uno per uno su ogni veicolo
            
            if isinstance(veicolo, Camion):  # se è un camion
                totale += Camion.costo_manutenzione()
                
            elif isinstance(veicolo, Furgone):  # se è un furgone
                totale += Furgone.costo_manutenzione()
                
            elif isinstance(veicolo, Motocarro):  # se è un motocarro
                totale += Motocarro.costo_manutenzione()
        print(f"Il costo totale delle manutenzioni è {totale} euro")

Veicolo=Camion("Prova", 0, 1500, 5)
Gestione=GestoreFlotta()  # creo l'oggetto gestore

print("------------MENU------------")
print("BENVENUTO SCEGLI LA TUA OPERAZIONE!")
scelta = int(input("1 aggiungi veicolo, 2 rimuovi veicolo, 3 costo totale, 4 verificare il peso, 5 riporta il carico a 0, 0 Esci "))

while scelta > 0:  # loop finché non sceglie 0

        if scelta == 1:
            Gestione.aggiungi_veicolo()
            print("------------------------------")

        elif scelta == 2:
            Gestione.rimuovi_veicolo()
            print("------------------------------")

        elif scelta == 3:
            Gestione.costo_totale_manutenzione()
            print("------------------------------")

        elif scelta == 4:
            peso=int(input("Quanto pesa il tuo veicolo? "))
            Veicolo.carico(peso)  # lo applico al veicolo fisso

        elif scelta == 5:
            Veicolo.scarica()  # svuoto il veicolo fisso
            print("Carico riportato a 0")

        else:
            print("pippo")

        scelta = int(input("1 aggiungi veicolo, 2 rimuovi veicolo, 3 costo totale, 4 verificare il peso, 5 riporta il carico a 0, 0 Esci "))   