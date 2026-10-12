class Libro:  #definisce la classe Libro

    def __init__(self, titolo, autore, pagine):  #costruttore
        self.titolo = titolo  #salva il titolo nell'istanza
        self.autore = autore  #salva l'autore nell'istanza
        self.pagine = pagine  #salva il numero di pagine nell'istanza

    def descrizione(self):  #metodo: restituisce una stringa con i dati del libro
        return (f"Il libro {self.titolo} è stato scritto da {self.autore} e ha in totale {self.pagine} pagine")


numeri = int(input("Quanti libri vuoi creare? Se non ne vuoi più creare digitare 0: "))  #legge da tastiera il numero di libri da creare
listaLibri = []  #crea una lista vuota per memorizzare gli oggetti Libro


while numeri != 0:  #ciclo: continua finché l'utente non digita 0

    for i in range(numeri):  #ciclo interno: ripete "numeri" volte
        titolo = input("Dimmi il titolo del libro: ")  #legge il titolo
        autore = input("Dimmi il nome dell'autore del libro: ")  #legge l'autore
        pagine = int(input("Dimmi il numero di pagine totali del libro: "))  #legge le pagine (come int)

        Libri = Libro(titolo, autore, pagine)  #crea un oggetto Libro con i dati inseriti
        listaLibri.append(Libri)  #aggiunge l'oggetto alla lista
        print("-------------------------------------------")  
        print(Libri.descrizione())  #stampa la descrizione del libro
        print("-------------------------------------------")  

    numeri = int(input("Quanti libri vuoi creare? Se non ne vuoi più creare digitare 0: "))  #chiede di nuovo quanti libri creare
