from abc import ABC, abstractmethod #classe ABC è in maiuscolo


class Pippo_Astratto(ABC):
    
    x=10
    
    @abstractmethod #DECORATORE
    def Metodo_Obbligatorio(self):      #Puo avere variabili e metodi reali MA NON GLI OGGETTI
        pass

    def ciao(self):
        print("ciao")
        
    @abstractmethod #DECORATORE
    def Metodo_Obbligatorio2(self):      #Puo avere variabili e metodi reali MA NON GLI OGGETTI
        pass

class Pippo_Reale(Pippo_Astratto):      #DEVE SOVRASCRIVERE TUTTI I METODI ASTRATTI
   
    def Metodo_Obbligatorio(self):
        print("Sono reale")
        
    def Metodo_Obbligatorio2(self):
        print("Sono reale 2")
        
        
P_r= Pippo_Reale()#dai figli si

#P_a=Pippo_Astratto() NON SI PUO' CREARE UN OGGETTO DELLA CLASSE ASTRATTA
