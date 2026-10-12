
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