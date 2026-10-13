import random  # importa il modulo per generare scelte casuali

class MembroSquadra:  # classe base per un membro generico della squadra

    def __init__(self, nome, eta):  # costruttore, salva nome e età
        self.nome = nome
        self.eta = eta

    def descrivi(self):  # stampa nome ed età
        print(f"Il giocatore si chiama {self.nome} e ha {self.eta} anni")

Membro = MembroSquadra("Generico", 0)  # crea un membro "vuoto"
Pl1 = MembroSquadra("Patrizio", 30)  # crea un membro con dati reali
Pl1.descrivi()  # lo stampa

class Squadra:  # classe che rappresenta un membro con la sua squadra

    def __init__(self, nome, eta, squadra):  # costruttore, salva anche la squadra
        self.nome = nome
        self.eta = eta
        self.squadra = squadra

    def squadra_stampa(self):  # stampa nome, età e squadra
        print(f"Il giocatore si chiama {self.nome}, ha {self.eta} anni e gioca nel {self.squadra}")

    # """ def __repr__(self):
    #     return f"Giocatore(nome={self.nome}, eta={self.eta}, squadra={self.squadra}) ha segnato" """
    

class Giocatore(Squadra):  # classe figlio di Squadra, rappresenta un giocatore

    def __init__(self, nome, eta, squadra, ruolo, numero_maglia):  # aggiunge ruolo e maglia
        super().__init__(nome, eta, squadra)  # chiama il costruttore del genitore
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia

    def __eq__(self, altro):  # definisce quando due giocatori sono "uguali": stessa squadra
        return self.squadra == altro.squadra

    def gioca_partita(self, squadra_avversaria):  # simula una partita a caso
        vincitrice = random.choice([self.squadra, squadra_avversaria])  # sceglie a caso chi vince, LA STAMPA E' BUGGATA!
        print(f"{vincitrice} ha vinto")

    def __getattribute__(self, name):  # si attiva a ogni lettura di attributo (qui non fa niente di speciale)
        return super().__getattribute__(name)  # delega al comportamento normale

class Allenatore(Squadra):  # classe figlio di Squadra, rappresenta un allenatore

    def __init__(self, nome, eta, squadra, anni_di_esperienza):  # aggiunge anni di esperienza
        super().__init__(nome, eta, squadra)
        self.anni_di_esperienza = anni_di_esperienza

    def dirige_allenamento(self):  # dice se allena bene in base all'esperienza
        if self.anni_di_esperienza >= 5:
            print(f"L'allenatore {self.nome} allena bene")
        else:
            print(f"L'allenatore {self.nome} non allena bene")

class Assistente(Squadra):  # classe figlio di Squadra, rappresenta un assistente

    def __init__(self, nome, eta, squadra, specializzazione):  # aggiunge la specializzazione
        super().__init__(nome, eta, squadra)
        self.specializzazione = specializzazione

    def supporto_team(self):  # dice cosa fa in base alla specializzazione
        if self.specializzazione == "Fisioterapia":
            print(f"L'Assistente {self.nome} è specializzato nella {self.specializzazione} e aiuta i giocatori nell'allenamento in caso di infortunio")
        elif self.specializzazione == "Analista di gioco":
            print(f"L'Assistente {self.nome} è specializzato nell' {self.specializzazione} per riportarli nei grafici durante e post partita")
        else:
            print(f"L'Assistente {self.nome} non è qualificato")

# --- Creazione oggetti e test ---

Squad = Squadra(" ", 0, " ")  # oggetto Squadra "vuoto"
Player = Giocatore("Pippo", 30, "Empoli", "Centrocampista", 12)  # giocatore 1
Player2 = Giocatore("Mario", 25, "Genoa", "Difensore", 7)  # giocatore 2
print(Player == Player2)  # False, squadre diverse
print("-----------------------------------------------")

Player3 = Giocatore("Lorenzo", 35, "Empoli", "Attaccante", 10)  # giocatore 3, stessa squadra di Player
Player3.squadra_stampa()  # stampa i suoi dati
print(Player == Player3)  # True, stessa squadra (Empoli)
print("-----------------------------------------------")

Player.gioca_partita(Player2)  # simula partita tra Empoli e Genoa

Allena = Allenatore("Giovanni", 45, "Milan", 6)  # allenatore con 6 anni di esperienza
print("-----------------------------------------------")
Allena2 = Allenatore("Marco", 25, "Torino", 3)  # allenatore con 3 anni
print("-----------------------------------------------")
Allena.dirige_allenamento()  # "allena bene" (>=5)
print("-----------------------------------------------")
Allena2.dirige_allenamento()  # "non allena bene" (<5)

Assist = Assistente("Marika", 23, "Milan", "Fisioterapia")  # assistente fisioterapista
print("-----------------------------------------------")
Assist2 = Assistente("Pietro", 20, "Sassuolo", " ")  # assistente senza specializzazione valida
print("-----------------------------------------------")
Assist3 = Assistente("Paola", 30, "Fiorentina", "Analista di gioco")  # assistente analista
Assist.supporto_team()  # stampa il messaggio di fisioterapia
print("-----------------------------------------------")
Assist2.supporto_team()  # stampa "non è qualificato"
print("-----------------------------------------------")
Assist3.supporto_team()  # stampa il messaggio di analista di gioco   