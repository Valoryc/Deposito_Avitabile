class Persona:                                        # Classe base (superclasse)


    def __init__(self):                               # Costruttore
        self.__nome="Pippo"                           # Attributo privato: nome (default "Pippo")
        self.__eta=10                                 # Attributo privato: eta' (default 10)

    def get_nome(self):                               # Getter del nome
        return self.__nome
                                                        # metodi get e set del nome
    def set_nome(self, nome):                         # Setter del nome
        self.__nome=nome
        
    def get_eta(self):                                # Getter dell'eta'
        return self.__eta
                                                        # metodi get e set dell'eta
    def set_eta(self, eta):                           # Setter dell'eta'
        self.__eta=eta
        
    
    def presentazione(self):                          # Stampa la presentazione
        print(f"{self.__nome} di anni {self.__eta} e' arrivato a scuola")
    
    
class Studente(Persona):                              # Classe ereditata da Persona
    
    def __init__(self):                               # Costruttore Studente
        super().__init__()                            # Richiama il costruttore di Persona
        self.__voti=[]                                # Attributo privato: lista voti (vuota)
        
    def get_voti(self):                               # Getter della lista voti
        return self.__voti
                                                        # metodi get e set dei voti
    def set_voti(self, voti):                         # Setter della lista voti
        self.__voti=voti
    
    def cambio_nome(self, nuovo_nome):                # Cambio nome tramite input
        nuovo_nome=input("Inserisci il vero nome: ")  # NB: parametro ignorato, sovrascritto da input
        self.set_nome(nuovo_nome)                     # Aggiorna nome con setter ereditato
        
    def cambio_eta(self, nuova_eta):                  # Cambio eta' tramite input
        nuova_eta=input("Inserisci la vera eta: ")    # NB: parametro ignorato, sovrascritto da input
        self.set_eta(nuova_eta)                       # Aggiorna eta' con setter ereditato
    
    def inserimento_voti(self):                       # Inserimento voti da tastiera
        lunghezza=int(input("Quanti voti vuoi inserire? "))  # Legge il numero di voti
        for i in range(lunghezza):                    # Ciclo per ogni voto da inserire
            voto = int(input(f"Inserisci il voto {i + 1}: "))  # Legge un singolo voto
            self.__voti.append(voto)                  # Aggiunge il voto alla lista
    
    def calcolo_media(self):                          # Calcolo e stampa della media
        somma=0                                       # Inizializza somma a zero
        for voto in self.__voti:                      # Scorre tutti i voti
            somma+=voto                               # Accumula la somma
        
        if self.__voti:                               # Controlla che ci siano voti
            media=somma/len(self.__voti)              # Calcola media = somma / quantita'
            print(f"La media e': ", media)            # Stampa la media
        else:
            print("Non sono stati inseriti voti.")    # Avviso se lista vuota
    
        

class Professore(Persona):                            # Classe ereditata da Persona
    
    def __init__(self):                               # Costruttore Professore
        super().__init__()                            # Richiama il costruttore di Persona
        self.__materia=" "                            # Attributo privato: materia (vuota)
        
    def get_materia(self):                            # Getter della materia
        return self.__materia
                                                        # metodi get e set della materia
    def set_materia(self, materia):                   # Setter della materia
        self.__materia=materia
        
    def cambio_nome(self, nuovo_nome):                # Cambio nome tramite input
        nuovo_nome=input("Inserisci il vero nome: ")  # NB: parametro ignorato, sovrascritto da input
        self.set_nome(nuovo_nome)                     # Aggiorna nome con setter ereditato
        
    def cambio_eta(self, nuova_eta):                  # Cambio eta' tramite input
        nuova_eta=input("Inserisci la vera eta: ")    # NB: parametro ignorato, sovrascritto da input
        self.set_eta(nuova_eta)                       # Aggiorna eta' con setter ereditato
        
    def registro_assenze(self):                       # Registro assenze alunni
        lista=[]                                      # Lista per risposte positive (non usata)
        cont=0                                        # Contatore assenti
        lunghezza=int(input("Quanti alunni hai in classe? "))  # Legge numero alunni
        for i in range(lunghezza):                    # Ciclo per ogni alunno
            risposta = input(f"L'alunno {i+1} e' assente? (si/no) ")  # Domanda assenza
            if risposta == "si" or risposta == "Si":                      # Confronto con "si" / "Si"
                lista.append(risposta)                # Aggiunge alla lista
                cont+=1                               # Incrementa contatore
                
        if cont>=1:                                   # Se almeno un assente
            print(f"Il numero di alunni assenti e' {cont}")  # Stampa contatore
  
                
    
print("-------------------------MENU----------------------------")  
Pers = Persona()                                        # Istanzia Persona (non usata)
Student=Studente()                                      # Istanzia Studente
Prof=Professore()                                       # Istanzia Professore

scelta = int(input("Vuoi 1 per Studente, 2 Professore (0 per uscire): "))  # Prima scelta utente


while scelta != 0:                                      # Ciclo fino a scelta == 0

    if scelta == 1:                                     # Branch: STUDENTE
        nome=input("Inserisci un nome: ")               # Legge il nome
        Student.cambio_nome(nome)                       # NB: parametro ignorato, fa nuovo input
        
        eta=int(input("Inserisci l'eta': "))            # Legge l'eta'
        Student.cambio_eta(eta)                         # NB: parametro ignorato, fa nuovo input
        
        Student.inserimento_voti()                      # Inserisce i voti
        Student.calcolo_media()                         # Calcola la media
        
        Student.presentazione()                         # Stampa presentazione

    elif scelta == 2:                                   # Branch: PROFESSORE
        nome=input("Inserisci un nome: ")               # Legge il nome
        Prof.cambio_nome(nome)                          # NB: parametro ignorato, fa nuovo input
        
        eta=int(input("Inserisci l'eta': "))            # Legge l'eta'
        Prof.cambio_eta(eta)                            # NB: parametro ignorato, fa nuovo input
        
        materia=input("Che materia insegni? ")          # Legge la materia
        Prof.get_materia()                              # NB: errore, dovrebbe essere set_materia(materia)
        
        Prof.registro_assenze()                         # Registra le assenze
        
        Prof.presentazione()                            # Stampa presentazione
        
    else:
        print("Errore di scelta")                       # Gestione scelta non valida

    # Aggiorna la scelta per il prossimo ciclo
    scelta = int(input("Vuoi 1 Studente, 2 Professore (0 per uscire): "))