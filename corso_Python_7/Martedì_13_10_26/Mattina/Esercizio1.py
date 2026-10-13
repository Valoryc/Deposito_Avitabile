#Classe con soli metodi statici: non serve né self né cls
class Convertitore:

    
    @staticmethod   #Metodo statico: non accede allo stato della classe né dell'istanza
    def euro_in_dollari(euro):
        dollar = euro * 1.08  #conversione euro dollari
        print(dollar)

    
    @staticmethod   #Metodo statico: converte chilometri in miglia
    def km_in_miglia(km):
        miglia = km * 0.621371  #conversione km miglia
        print(miglia)



euro = int(input("Quale cifra vuoi convertire in dollari? "))    #Legge l'importo in euro da input

Conversione = Convertitore.euro_in_dollari(euro)  #Chiama il metodo statico direttamente sulla classe


km = int(input("Quanti km vuoi convertire in miglia? "))    #Legge i chilometri da input

Chilometri = Convertitore.km_in_miglia(km)  #Chiama il metodo statico direttamente sulla classe 