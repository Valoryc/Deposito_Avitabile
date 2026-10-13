class parametri_privati():
    
    #variabile privata
    __nome = "Giada"
    
    _protetto = "nina"

    def __init__(self,nome):
        self.__nome=nome
    
    #get e set
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, come_nuovo):
        if len(come_nuovo)<0 :
            print("Sei scemo")
        else:
            self.__nome=come_nuovo
            self.__metodoprivato() 
        
    #metodo privato richiamato nei metodi pubblici
    def __metodoprivato(self):
        print("sono dentro")    
    
    
O_pp= parametri_privati("giada")
print(O_pp.get_nome())
O_pp.set_nome("pippo")
print(O_pp.get_nome())

print(O_pp._protetto)

    