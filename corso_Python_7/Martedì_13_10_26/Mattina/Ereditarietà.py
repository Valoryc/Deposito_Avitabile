""" class Animale:
    
    def __init__(self,nome):
        self.nome=nome
        
    def parla(self):
        print(f"{self.nome} fa suono generico")
        

class Cane(Animale):
    
    def parla(self):
        print (f"{self.nome} abbaia! ")
        
        
Animale_generico=Animale("AnimaleGenerico")
Can=Cane("Filippo")


Animale_generico.parla()
Can.parla() """


class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")

class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni

    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")

class AutomobileSportiva(Veicolo,DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self,marca,modello)
        DotazioniSpeciali.__init__(self,dotazioni)
        self.cavalli=cavalli
        
    def mostra_dotazioni(self):
        super().mostra_informazioni() 
        print(f"Potenza; {self.cavalli} CV")
        self.mostra_dotazioni()
        
Auto_sportiva = AutomobileSportiva("BMW", "M3" , [" ABS", "CONTROLLO TRAZIONE", "AIRBAG"], 750)
Auto_sportiva.mostra_informazioni()