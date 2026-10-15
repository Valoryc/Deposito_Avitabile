from abc import ABC, abstractmethod

class Impiegato(ABC):
    
    def __init__(self,nome,cognome,stipendio_base):
        self.nome=nome
        self.cognome=cognome
        self.stipendio_base=stipendio_base
        
    @abstractmethod
    def calcola_stipendio(self):
        pass
    
    def riepilogo(self):
        return "Stampa generica"
    
class Impiegato_Fisso(Impiegato):
    
    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)
    
    def calcola_stipendio(self):
        return self.stipendio_base
    
    def riepilogo(self):          
        print(f"Lo stipendio di {self.nome} {self.cognome} è di {self.stipendio_base} euro")
    
class Impiegato_A_Provvigione(Impiegato):
    
    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)
    
    def calcola_stipendio(self,bonus):
        return self.stipendio_base+bonus
    
    def riepilogo(self):          
        print(f"Lo stipendio di {self.nome} , {self.cognome} è di {self.stipendio_base} euro")
    
    
scelta=int(input("Sei un'Impiegato Fisso(1) o a Provvigione(2)? "))



if scelta == 1:
    nome=input("Inserisci il nome dell'impiegato: ")
    cognome=input("Inserisci il cognome dell'impiegato: ")
    stipendio_base=float(input("Quanto hai di stipendio base? "))
    Impiegato_fiss=Impiegato_Fisso(nome,cognome,stipendio_base)
    Impiegato_fiss.riepilogo()
    
elif scelta == 2:
    nome=input("Inserisci il nome dell'impiegato: ")
    cognome=input("Inserisci il cognome dell'impiegato: ")
    stipendio_base=float(input("Quanto hai di stipendio base? "))
    Impiegato_provv=Impiegato_A_Provvigione(nome,cognome,stipendio_base)
    bonus=int(input("Quanto percepisci di bonus? Scrivi la cifra "))
    stipendio_totale=Impiegato_provv.calcola_stipendio(bonus)
    print(f"Lo stipendio di {nome} {cognome} è di {stipendio_totale} euro")
    
else:
    
    print("sei un pippo")