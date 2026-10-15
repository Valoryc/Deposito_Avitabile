from abc import ABC, abstractmethod  # import per fare classi astratte

class Impiegato(ABC):  # classe astratta base, non si può creare direttamente

    def __init__(self, nome, cognome, stipendio_base):
        self.nome=nome
        self.cognome=cognome
        self.stipendio_base=stipendio_base

    @abstractmethod
    def calcola_stipendio(self):  # ogni classe figlia DEVE riscriverlo
        pass

    def riepilogo(self):  # metodo generico, le figlie lo possono sovrascrivere
        return "Stampa generica"

class Impiegato_Fisso(Impiegato):  # impiegato fisso eredita da Impiegato

    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)  # chiamo il __init__ del genitore

    def calcola_stipendio(self):  # il fisso prende solo lo stipendio base
        return self.stipendio_base

    def riepilogo(self):  # sovrascrivo il metodo del genitore
        print(f"Lo stipendio di {self.nome} {self.cognome} è di {self.stipendio_base} euro")

class Impiegato_A_Provvigione(Impiegato):  # impiegato a provvigione eredita da Impiegato

    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)

    def calcola_stipendio(self, bonus):  # qui serve anche il bonus come parametro
        return self.stipendio_base+bonus

    def riepilogo(self):  # sovrascrivo il metodo del genitore
        print(f"Lo stipendio di {self.nome} , {self.cognome} è di {self.stipendio_base} euro")


scelta=int(input("Sei un'Impiegato Fisso(1) o a Provvigione(2)? "))  # chiedo che tipo di impiegato è


if scelta == 1:  # se è fisso
    nome=input("Inserisci il nome dell'impiegato: ")
    cognome=input("Inserisci il cognome dell'impiegato: ")
    stipendio_base=float(input("Quanto hai di stipendio base? "))
    Impiegato_fiss=Impiegato_Fisso(nome,cognome,stipendio_base)  # creo l'oggetto
    Impiegato_fiss.riepilogo()  # stamppo il riepilogo

elif scelta == 2:  # se è a provvigione
    nome=input("Inserisci il nome dell'impiegato: ")
    cognome=input("Inserisci il cognome dell'impiegato: ")
    stipendio_base=float(input("Quanto hai di stipendio base? "))
    Impiegato_provv=Impiegato_A_Provvigione(nome,cognome,stipendio_base)  # creo l'oggetto
    bonus=int(input("Quanto percepisci di bonus? Scrivi la cifra "))
    stipendio_totale=Impiegato_provv.calcola_stipendio(bonus)  # calcolo base+bonus
    print(f"Lo stipendio di {nome} {cognome} è di {stipendio_totale} euro")

else:  # se non sceglie 1 o 2
    print("sei un pippo")   