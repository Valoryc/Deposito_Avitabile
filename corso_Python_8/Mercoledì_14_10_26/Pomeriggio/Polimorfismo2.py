class Posto():      #classe base
    
    __numeroPosti=0
    __fila=0                #attributi privati
    __occupato= False
    
    def __init__(self,numero,fila):
        self.__numeroPosti=numero       #costruttore con gli attributi privati
        self.__fila=fila
    
    def prenota(self):      #metodo prenota posto vuoto
        pass
    
    def libera(self):   #metodo verifica posto vuoto
        pass
    
    def get_risultati(self):    #get vuoto
        pass
    

class PostoStandard(Posto): #classe figlio Posto
    
    def __init__(self, numero, fila, costo):    #costruttore
        super().__init__(numero, fila)          #richiamata delle variabili del padre
        self.costo=11.50                        #assegnazione valore costo (Boh non so se è ok)
        
    def prenota(self,numero,fila):              #metodo prenota posto
        if Teatro.prenota_posto == PostoStandard.prenota:   #TENTATIVO DI IF!!
            Posto.__occupato=True   #se occupato passa a true (?????)
            print("Posto Occupato")
        
        else:
            
            print(Teatro.__posto)   #tentato di stampare la lista, probabilmente sbagliato
            
        
        
    

class Teatro(): #classe a parte dalle altre
    
    __posto=[]  #lista dei posti!!
    
    def aggiungi_posto(self,posto):     #Metodo aggiungi posto corretto, GRAZIE MIRKO!!!!!
        numero=int(input("Inserisci il numero del posto: "))
        fila=int(input("Inserisci la fila del posto: "))
        Posto_inserito=Posto(numero,fila)
        
        self.__posto.append(Posto_inserito)
        
        
    
    def prenota_posto(self):    #Metodo prenota posto correto, di nuovo GRAZIE MIRKO!!!!!
        numero=int(input("Inserisci il numero del posto: "))
        fila=int(input("Inserisci la fila del posto: "))
        PostoStandard.prenota(numero,fila)
    
    def stampa_posti_occupati(): #metodo stampa vuoto
        pass