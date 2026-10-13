class Animale:
    numero_animali = 0  #Attributo di classe: contatore globale condiviso da tutte le istanze

    
    def __init__(self, nome, specie):    #Costruttore: chiamato automaticamente a ogni istanziazione                                                                                                                     
        self.nome = nome        #attributo di istanza: nome specifico di questo animale
        self.specie = specie    #attributo di istanza: specie specifica di questo animale
        Animale.numero_animali += 1  #incrementa il contatore di classe

   
    @classmethod     #Metodo di classe: si chiama sulla classe, non su un'istanza
    def quanti_animali(cls):    #cls si riferisce alla classe Animale
        return f"Numero di animali creati: {cls.numero_animali}"


numero = int(input("Quanti animali vuoi inserire? "))   #Legge da input quante istanze creare


while numero > 0:   #Ciclo: crea un oggetto Animale per ogni iterazione
    nome = input("Inserisci il nome dell'animale: ")
    specie = input("Inserisci la specie dell'animale: ")
    animale = Animale(nome, specie)  #istanzia un nuovo oggetto
    numero -= 1  #decrementa per uscire dal ciclo


print(Animale.quanti_animali())   #Stampa il totale degli animali creati (chiamata diretta sulla classe)