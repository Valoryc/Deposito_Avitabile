x = 30

x = "pippo"


class Pippo():
    def fai_cose_a_caso(self):
        print("Pippa")
    
class Pippa():
    def fai_cose_a_caso(self):
        print("Pozzo")
        
        
pippo=Pippo()
pippa=Pippa()

def fai_cose(oggetto_casuale):
    
    oggetto_casuale.fai_cose_a_caso()
    
fai_cose(pippo)

fai_cose(pippa)