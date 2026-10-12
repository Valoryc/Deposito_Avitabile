class Automobile:
    
    numero_di_ruote = 4
    
    def __init__(self, marca,modello):
        
        self.marca=marca
        self.modello=modello
        
    def stampa_info(self):
        
        print("L'automobile è una: ", self.marca , self.modello)
        
Auto1 = Automobile("BMW", "M3")
Auto2 = Automobile("Mercedes-Benz", "Buh")
Auto1.stampa_info()
Auto2.stampa_info()

class Contatore:
    numero_istante = 0
    
    def __init__(self):
        Contatore.numero_istante += 1
        
    @classmethod
    def mostra_numero_istanze (cls):
        print(f"Sono state create {cls.numero_istante} istanze")
        
C1=Contatore()
C2=Contatore()

Contatore.mostra_numero_istanze()