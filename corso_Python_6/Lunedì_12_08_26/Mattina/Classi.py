class Person:
    
    #Metodo costruttore
    def __init__(self, eta, nome):
        self.eta = eta
        self.nome=nome

    #Variabile 
    cittadinanza = " "
    
    #Metodo normale
    def saluta(self):
        return ("Ciao Mirko")

Ogg_1 = Person("Pippo",15)
Ogg_2 = Person("Mirta",45)


print(Ogg_1.nome)
print(Ogg_2.nome)

print(Ogg_1.saluta())






class Calcolatrice:
    
    @staticmethod
    def somma (a,b):
        return a+b

risultato = Calcolatrice.somma(10,3)

print(risultato)






