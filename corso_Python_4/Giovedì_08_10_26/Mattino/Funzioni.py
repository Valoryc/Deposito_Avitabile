#Esempi di funzioni

def marcoSaluta(nome):
    print("Ciao ", nome)
    
def saluti(nome):
    print("Buongiorno ", nome)
    
def somma (a,b):
    somma=a+b
    print(somma)
    
def sottrazione (a,b):
    sottrazione=a-b
    print(sottrazione)

def marcoSaluta (nome:str):
    print("Ciao ", nome)
    
def sottrazione (a =0, b= 0):
    sottrazione=a-b
    print(sottrazione)

def moltiplicazione (a,b):
    return a*b


x=int(input("Inserisci il primo numero "))
x2=int(input("Inserisci il secondo numero "))


marcoSaluta("Giulia")
saluti("Ettore")
somma(4,6)
sottrazione(20)
print(moltiplicazione(x,x2))

