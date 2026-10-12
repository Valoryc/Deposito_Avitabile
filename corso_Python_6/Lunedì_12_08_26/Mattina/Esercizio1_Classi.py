import math  #importa il modulo math per usare sqrt (radice quadrata)

class Punto:  #definisce la classe Punto

    def __init__(self, x, y):  #costruttore
        self.x = x  #salva la coordinata x nell'istanza
        self.y = y  #salva la coordinata y nell'istanza

    def muovi(self, dx, dy):  #metodo: sposta il punto di dx e dy
        self.x += dx  #aggiorna x sommando dx
        self.y += dy  #aggiorna y sommando dy

    def distanza_da_origine(self):  #metodo: calcola la distanza dall'origine (0,0)
        return math.sqrt(self.x**2 + self.y**2)  #teorema di Pitagora


x = 0  #coordinata iniziale x
y = 0  #coordinata iniziale y

dx = int(input("Inserisci un valore per la tua dx: "))  #legge da tastiera lo spostamento in x
dy = int(input("Inserisci un valore per la tua dy: "))  #legge da tastiera lo spostamento in y

Punt = Punto(x, y)  #crea un oggetto Punto con coordinate (0, 0)
print(f"Le coordinate del punto: ({Punt.x}, {Punt.y})")  #stampa (0, 0)

Punt.muovi(dx, dy)  #sposta il punto dei valori inseriti
print(f"Le coordinate del punto: ({Punt.x}, {Punt.y})")  #stampa le nuove coordinate
print("La distanza dall'origine è: ", Punt.distanza_da_origine())  #stampa la distanza   