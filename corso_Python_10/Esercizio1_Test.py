# Classe base: rappresenta un elettrodomestico generico
class Elettrodomestica:
    
    def __init__(self, marca, modello, anno_acquisto, guasto):
        # Attributi privati (doppio underscore): accessibili solo tramite getter/setter
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto
        
    # --- Getter e Setter ---
    
    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca
        
    def get_modello(self):
        return self.__modello

    def set_modello(self, modello):
        self.__modello = modello
        
    def get_anno(self):
        return self.__anno_acquisto

    def set_anno(self, anno_acquisto):
        while anno_acquisto > 2026:
            print("Anno sbagliato, inserisci un anno valido (<= 2026)")     #controllo se l'anno inserito è maggiore del 2026, se così fosse si richiede un anno minore o uguale al 2026
            anno_acquisto = int(input("Anno di acquisto: "))
        self.__anno_acquisto = anno_acquisto
        
    def get_guasto(self):
        return self.__guasto

    def set_guasto(self, guasto):
        self.__guasto = guasto
        
    # Restituisce una descrizione testuale dell'elettrodomestico
    def descrizione(self):
        return f"{self.__marca} {self.__modello}, {self.__anno_acquisto}, guasto: {self.__guasto}"   
        
    # Costo base di 100 euro, le sottoclassi lo sovrascrivono (polimorfismo)
    def stima_costo_base(self, costo=100):
        print(f"Il costo base è di {costo} euro")
        return costo
        
# Sottoclasse: Lavatrice (eredita da Elettrodomestica)
class Lavatrice(Elettrodomestica):
    
    def __init__(self, marca, modello, anno_acquisto, guasto, capacita_kg, giri_centrifuga):
        super().__init__(marca, modello, anno_acquisto, guasto)  # chiama il costruttore del padre
        self.__capacita_kg = capacita_kg
        self.__giri_centrifuga = giri_centrifuga
    
    def get_capacita(self):
        return self.__capacita_kg

    def set_capacita(self, capacita_kg):
        self.__capacita_kg = capacita_kg
        
    def get_giri(self):
        return self.__giri_centrifuga

    def set_giri(self, giri_centrifuga):
        self.__giri_centrifuga = giri_centrifuga
    
    # Override: costo maggiorato se capacità > 5kg OPPURE giri >= 1400
    def stima_costo_base(self):
        if self.__capacita_kg > 5 or self.__giri_centrifuga >= 1400: 
            costo_Lavatrice = 165
            print("Prezzo Aggiornato")
            # Passa il proprio costo al metodo del padre
            return super().stima_costo_base(costo_Lavatrice)
        else:
            return super().stima_costo_base()
            
    def descrizione(self):
        return super().descrizione()
            
# Sottoclasse: Frigorifero (eredita da Elettrodomestica)
class Frigorifero(Elettrodomestica):
    
    def __init__(self, marca, modello, anno_acquisto, guasto, litri):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__litri = litri
        self.__ha_freezer = False  # default: senza freezer, poi chiesto all'utente
        
    def get_litri(self):
        return self.__litri
    
    def set_litri(self, litri):
        self.__litri = litri

    def get_freezer(self):
        return self.__ha_freezer
    
    # Override: costo maggiorato se ha freezer OPPURE litri > 1000
    def stima_costo_base(self):
        litri_Max = 1000  # soglia oltre la quale il costo aumenta
        self.__ha_freezer = input("Il tuo frigo ha il freezer? si/no ")
        if self.__ha_freezer == "si" or self.__litri > litri_Max:
            costo_Frigorifero = 200
            print("Prezzo Aggiornato")
            return super().stima_costo_base(costo_Frigorifero)
        else:
            return super().stima_costo_base()
            
    def descrizione(self):
        return super().descrizione()
    
# Sottoclasse: Forno (eredita da Elettrodomestica)
class Forno(Elettrodomestica):
            
    def __init__(self, marca, modello, anno_acquisto, guasto, tipo_alimentazione):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__tipo_alimentazione = tipo_alimentazione  # "elettrico" o "gas"
        self.__ha_ventilato = False  # default: non ventilato, poi chiesto all'utente
        
    def get_alimentazione(self):
        return self.__tipo_alimentazione
    
    def set_alimentazione(self, tipo_alimentazione):
        self.__tipo_alimentazione = tipo_alimentazione

    def get_ventilazione(self):
        return self.__ha_ventilato
        
    # Override: costo diverso in base ad alimentazione e ventilazione
    def stima_costo_base(self):
        self.__ha_ventilato = input("Il tuo forno è ventilato? si/no ")
        if self.__ha_ventilato == "si" or self.__ha_ventilato == "Si":
            # Forno ventilato: costo dipende dall'alimentazione
            if self.__tipo_alimentazione == "gas":
                costo_Forno = 190
                print("Prezzo Aggiornato")
                return super().stima_costo_base(costo_Forno)
            elif self.__tipo_alimentazione == "elettrico":
                costo_Forno = 240
                print("Prezzo Aggiornato")
                return super().stima_costo_base(costo_Forno)
            else:
                # Alimentazione non riconosciuta: non restituisce nulla
                return super().stima_costo_base()
        else:
            # Forno non ventilato: costo base
            return super().stima_costo_base()
            
    def descrizione(self):
        return super().descrizione()
    

# Classe che associa un elettrodomestico a un ticket di riparazione
class TicketRiparazione:
    
    def __init__(self, id_ticket, elettrodomestico):
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico  # oggetto di tipo Elettrodomestica o sottoclasse
        self.__stato = "aperto"  # stato iniziale del ticket
        self.__note = []  # lista di note, inizialmente vuota
        
    def get_stato(self):
        return self.__stato
    
    def set_stato(self, stato):
        # Controlla che lo stato attuale sia valido prima di modificarlo
        if stato in ("aperto", "in lavorazione", "chiuso"):
            self.__stato=stato
        else:
            print("Stato in valido")
            
    def get_note(self):
        return self.__note
    
    def set_note(self):
        self.__note = []  # resetta le note
        
    def get_id(self):
        return self.__id_ticket
    
    def set_id(self, id_ticket):
        self.__id_ticket = id_ticket
        
    # Restituisce l'oggetto elettrodomestico associato (usato da Officina per type/isinstance)
    def get_elettro(self):
        return self.__elettrodomestico
        
    def aggiungi_note(self):
        agg_nota = input("Inserisci una nota: ")
        self.__note.append(agg_nota)  # aggiunge la nota in fondo alla lista
        
    
    #Utilizziamo *voci_extra per raccogliere un determinato numero di elementi senza dover riscrivere altre volte lo stesso metodo (Tupla)
    def calcola_preventivo(self, *voci_extra):
        totale = self.__elettrodomestico.stima_costo_base()  # polimorfismo: ogni tipo ha il suo costo
        for voce in voci_extra:
            totale += voce
        return totale   

# Classe che gestisce l'officina: lista di ticket e operazioni su di essi
class Officina:
    
    def __init__(self):
        self.__nome = " "
        self.__tickets = []  # lista che conterrà gli oggetti TicketRiparazione
        
    def get_nome(self):
        return self.__nome
    
    def get_ticket(self):
        return self.__tickets
        
    # Aggiunge un ticket alla lista interna
    def aggiungi_ticket(self, ticket):
        self.__tickets.append(ticket)
        
    # Cerca il ticket per ID e lo chiude
    def chiudi_ticket(self, id_ticket):
        for ticket in self.__tickets:
            if ticket.get_id() == id_ticket:
                ticket.set_stato("chiuso")
                print("Ticket chiuso")
                break  # trovato: esce subito dal ciclo
        else:
            # else del for: si esegue solo se NON è stato trovato (nessun break)
            print("Ticket non trovato")
            
    # Somma i preventivi di tutti i ticket (polimorfismo: ogni elettrodomestico calcola il suo costo)
    def totale_preventivi(self):
        totale = 0
        for ticket in self.__tickets:
            totale += ticket.calcola_preventivo()
        return totale

    # Usa isinstance() per classificare gli elettrodomestici per tipo e contare i ticket
    def statistiche_per_tipo(self):
        lavatrici = 0
        frigoriferi = 0
        forni = 0

        for ticket in self.__tickets:
            elettro = ticket.get_elettro()  # recupera l'oggetto elettrodomestico
            if isinstance(elettro, Lavatrice):       # verifica il tipo dell'oggetto
                lavatrici += 1
            elif isinstance(elettro, Frigorifero):
                frigoriferi += 1
            elif isinstance(elettro, Forno):
                forni += 1

        print(f"Numero di lavatrici in riparazione/riparate: {lavatrici}")
        print(f"Numero di frigoriferi in riparazione/riparate: {frigoriferi}")
        print(f"Numero di forni in riparazione/riparate: {forni}")   
        

Elettro=Elettrodomestica(" "," ",0," ")
Officine=Officina()  # crea l'istanza dell'officina

print("------------MENU------------")
print("BENVENUTO NELL'OFFICINA!!")

# Prima lettura della scelta
scelta = int(input("1 Aggiungi ticket, 2 Chiudi ticket, 3 Totale preventivi, 4 Statistiche per tipo, 6 Esci "))

# Ciclo principale: si ripete finché l'utente non sceglie 6 (Esci)
while scelta >= 1 and scelta < 5:

    if scelta == 1:
        # Costruisce l'oggetto Elettrodomestico in base al tipo scelto dall'utente
        tipo = int(input("1 Lavatrice, 2 Frigorifero, 3 Forno: "))
        marca = input("Marca: ")
        modello = input("Modello: ")
        anno = int(input("Anno di acquisto: "))
        Elettro.set_anno(anno)
        guasto = input("Descrivi il guasto: ")


        # In base al tipo, crea l'oggetto della sottoclasse corretta
        if tipo == 1:
            capacita = int(input("Capacità kg: "))
            giri = int(input("Giri centrifuga: "))
            elettro = Lavatrice(marca, modello, anno, guasto, capacita, giri)
        elif tipo == 2:
            litri = int(input("Litri: "))
            elettro = Frigorifero(marca, modello, anno, guasto, litri)
        elif tipo == 3:
            alimentazione = input("Alimentazione (elettrico/gas): ")
            elettro = Forno(marca, modello, anno, guasto, alimentazione)

        # Crea il ticket associando l'ID e l'elettrodomestico
        id_ticket = int(input("ID ticket: "))
        ticket = TicketRiparazione(id_ticket, elettro)
        Officine.aggiungi_ticket(ticket)  # aggiunge il ticket all'officina
        print("------------------------------")

    elif scelta == 2:
        id_ticket = int(input("ID del ticket da chiudere: "))
        Officine.chiudi_ticket(id_ticket)
        print("------------------------------")
        
    elif scelta == 3:
        Officine.totale_preventivi()
        print("------------------------------")

    elif scelta == 4:
        Officine.statistiche_per_tipo()
        print("------------------------------")

    else:
        # Scelta non valida 
        print("pippo")

    # Ripropone il menu a ogni iterazione del ciclo
    scelta = int(input("1 Aggiungi ticket, 2 Chiudi ticket, 3 Totale preventivi, 4 Statistiche per tipo, 5 Esci "))      