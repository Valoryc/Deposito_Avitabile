""" class Studente:
    
    def __init__(self, nome, eta):
        self.nome=nome
        self.eta=eta
        
    def __str__(self):
        return "Studente " + self.nome + ", età: " + str(self.eta)
    
    
Studente1=Studente("Giappippo", 29)

print(Studente1) """

""" class Squadra:
    
    def __init__(self,nome,giocatori):
        self.nome=nome
        self.giocatori=giocatori
        
    def __len__(self):
        return len(self.giocatori)
    

Squadra1 = Squadra("Tigri" , ["Luca","Mirko","Pippo"])

print(len(Squadra1)) """


class Moltiplicatore:
    
    def __init__(self,numero):
        self.numero=numero
    
    def __call__(self, valore):
        return valore * self.numero
    
Doppio = Moltiplicatore(5)

print(Doppio(13))