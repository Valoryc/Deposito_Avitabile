#Prova delle Variabili e i suoi tipi

nomeVariabile = "valore o valori"
numero= 1 

print("--------------------------------------------------")


#Stampa di variabili di una stringa
s = "Facebook"

print(s[4])
print(s[7])

print("--------------------------------------------------")


#Utilizzo di alcuni metodi delle stringhe
p= "Sono vegetariana"
print(len(p)) #lunghezza della stringa
print(p.upper()) #converte la stringa in maiuscolo
print(p.split(",")) #separa la stringa
print(p.replace("vegetariana", "erbivora")) #sosituisce una parola con un'altra

print("--------------------------------------------------")

#Prova di metodi su nomeVariabile
print(nomeVariabile.capitalize())
print(nomeVariabile.istitle())
print(nomeVariabile.find("valori"))
print(nomeVariabile.count("a"))

print("--------------------------------------------------")


#Prova di concatenare due stringhe
arrivederci = "Ci vediamo presto"
nome= "Giovanni"

mess= arrivederci + " " + nome
print(mess)

print("--------------------------------------------------")


#Prova variabili di tipo booleano e con le sue operazioni   
x=9
y=27

print(x == y)
print(x != y)
print (x > y)
print (x < y)
print (x >= y)
print (x <= y)

print("--------------------------------------------------")

#Prova di controlli con booleani
x=8
y=16
z=8

print (x < y and y > z)
print (x < y or y > z)
print (not(x < y and y > z))



