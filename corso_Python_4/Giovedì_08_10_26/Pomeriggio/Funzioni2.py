#GENERATORI e DECORATIVI

def decoratore(funzione):
    def wrapper():
        funzione()
        print("Prima dell'esecuzione della funzione")
        print("Dopo l'esecuzione della funzione")
    return wrapper

                                    #funzione() == saluta()
@decoratore
def saluta():
    print("Ciao!")

saluta()


def conta_fino_a(numero_massimo):

    numero = 1

    while numero <= numero_massimo:

        yield numero

        numero = numero + 1