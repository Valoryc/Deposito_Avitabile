class Animale:  #Classe base  da cui ereditano le classi figlie

    
    def __init__(self, nome, eta):  #Metodo costruttore
        self.nome = nome          #attributo: il nome dell'animale
        self.eta = eta            #attributo: l'età dell'animale

    
    def fai_suono(self):    #Metodo che fa emettere un suono generico
        print(f"{self.nome} fa suono generico")



class Leone(Animale):   #Classe Leone che EREDITA da Animale

    
    def __init__(self, nome, eta, caccia):  #Costruttore del Leone: aggiunge un attributo extra (caccia)
        super().__init__(nome, eta)  #chiama il costruttore del genitore (Animale)
        self.caccia = caccia         #attributo specifico del Leone: metodo di caccia

    
    def come_caccia(self):  #Metodo specifico del Leone
        print(f"Il leone sta cacciando con {self.caccia}")



class Giraffa(Animale): #Classe Giraffa che EREDITA da Animale

    def __init__(self, nome, eta, mangiare):    #Costruttore della Giraffa: aggiunge un attributo extra (mangiare)
        super().__init__(nome, eta)  #richiama il costruttore di Animale
        self.mangiare = mangiare     #attributo specifico: come mangia

    
    def come_mangia(self):  #Metodo specifico della Giraffa
        print(f"La giraffa sta mangiando in modo {self.mangiare}")



class Pinguino(Animale):    #Classe Pinguino che EREDITA da Animale

    def __init__(self, nome, eta, scivolare):   #Costruttore del Pinguino: aggiunge un attributo extra (scivolare)
        super().__init__(nome, eta)  #richiama il costruttore di Animale
        self.scivolare = scivolare   #attributo specifico: come scivola

    
    def come_scivolare(self):   #Metodo specifico del Pinguino
        print(f"Il pinguino sta scivolando {self.scivolare}")



Animale_generico = Animale("Animale", 0)        #istanza della classe base
Leon = Leone("Franco", 2, "astuzia")            #istanza di Leone
Leon.come_caccia()                               #chiama il metodo del Leone
print("-----------------------------------")     
Giraffe = Giraffa("Luisa", 4, "lento le foglie")  #istanza di Giraffa
Giraffe.come_mangia()                              #chiama il metodo della Giraffa
print("-----------------------------------")
Penguin = Pinguino("Pippo", 6, "velocemente")    #istanza di Pinguino
Penguin.come_scivolare()                          #chiama il metodo del Pinguino   