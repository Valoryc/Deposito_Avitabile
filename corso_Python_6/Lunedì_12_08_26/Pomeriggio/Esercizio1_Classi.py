class ContoCorrente:
    
    def __init__(self, intestatario, saldo):
        self.intestatario = intestatario
        self.saldo = saldo

    def deposita(self, importo):
        self.saldo += importo

    def preleva(self, importo):
        if importo > self.saldo:
            print("Fondi insufficienti")
        else:
            self.saldo -= importo

    def visita_contocorrente(self):
        return f"Il saldo di {self.intestatario} è di: {self.saldo} euro"


print("-------------------------MENU----------------------------")
intestatario = input("BENVENUTO INSERISCI IL TUO NOME: ")
Conto = ContoCorrente(intestatario, 0)  # creato UNA volta, saldo iniziale 0

scelta = int(input("Vuoi 1 depositare, 2 prelevare o 3 visualizzare? (0 per uscire): "))

while scelta != 0:
    if scelta == 1:
        importo = float(input("Inserisci il valore che vuoi depositare: "))
        if importo <= 0:
            print("Importo invalido")
        else:
            Conto.deposita(importo)

    elif scelta == 2:
        importo = float(input("Inserisci il tuo importo: "))
        Conto.preleva(importo)

    elif scelta == 3:
        print(Conto.visita_contocorrente())

    else:
        print("Errore di scelta")

    scelta = int(input("Vuoi 1 depositare, 2 prelevare o 3 visualizzare? (0 per uscire): "))   