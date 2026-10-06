#Esercizio 1

numero = int(input("Inserisci un numero: "))
numeroVirgola= float(input("Inserisci un numero con la virgola: "))
frase = input("Inserisci una frase: ")
numBoolean= bool(input("Inserisci un valore booleano True o False: "))
carattere = input("Inserisci un carattere: ")

print(numero , "|" , numeroVirgola, "|" , frase , "|" , numBoolean, "|" , carattere)

print("---------------------------------")

num1 = int(input("Inserisci un numero: "))
num2 = int(input("Inserisci un altro numero: "))

print(num1 < num2 and num1 > num2)
print(num1 < num2 or num1 > num2 or num1 == num2)
print(not(num1 < num2 and num1 > num2))
