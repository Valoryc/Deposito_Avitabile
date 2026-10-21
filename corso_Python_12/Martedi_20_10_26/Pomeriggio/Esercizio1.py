import numpy as np  #importazione della libreria NumPy

righe=int(input("Quante righe vuoi nella matrice? "))
colonne=int(input("Quante colonne vuoi nella matrice? "))

n_inizio=int(input("Scegli numero iniziale: "))
n_fine=int(input("Scegli numero finale: "))

matrice=np.arange(n_inizio,n_fine).reshape(righe,colonne)  #Creazione della matrice

print("------------MENU------------")  #Menu
print("BENVENUTO SCEGLI LA TUA OPERAZIONE!")

scelta = int(input("1 Visualizza matrice, 2 Sottomatrice centrale, 3 Trasposta, 4 Somma, 5 Moltiplicazione element-wise, 6 Media, 7 Determina la matrice, 8 Esci: "))

while scelta !=  8:
    if scelta == 1:
        print(matrice)  #Visualizza la matrice

    elif scelta == 2:
        centro_r = matrice.shape[0] // 2  #Calcola il centro delle righe attraverso una divisione intera con il 2
        centro_c = matrice.shape[1] // 2  #Calcola il centro delle colonne  attraverso una divisione intera con il 2
        print(matrice[centro_r-1:centro_r+1, centro_c-1:centro_c+1])  #Visualizza la sottomatrice centrale attraverso il calcolo delle posizioni:
                                                                        #se centro_r è 5 nel print sarà 4:6 e così anche il centro_c

    elif scelta == 3:
        trasposta = matrice.T  #Trasposizione della matrice
        print(trasposta)

    elif scelta == 4:
        sum_value=np.sum(matrice)  #Somma di tutti gli elementi
        print(sum_value)

    elif scelta == 5:
        scelta2=input("Vuoi creare una seconda matrice delle stesse dimensioni della prima? ")
        if scelta2 == "Si" or scelta2 == "si":
            righe_2=righe
            colonne_2=colonne

            n_inizio2=n_inizio
            n_fine2=n_fine

            matrice2=np.arange(n_inizio2,n_fine2).reshape(righe_2,colonne_2)  #Creazione della seconda matrice

            element=matrice*matrice2  #Moltiplicazione element-wise
            print(element)
        else:
            break

    elif scelta == 6:
        mean_value=np.mean(matrice2)  #Calcolo della media della seconda matrice
        print(mean_value)
  
    elif scelta == 7:
        determinante=np.linalg.det(matrice)  #Calcolo della determinante della prima matrice
        print("La determinante è: ",determinante)

    else:
        print("Scelta errata")

    print("------------------------------")
    scelta = int(input("1 Visualizza matrice, 2 Sottomatrice centrale, 3 Trasposta, 4 Somma, 5 Moltiplicazione element-wise, 6 Media, 7 Determina la matrice, 8 Esci: "))  #Riproposta di scelta

print("Uscita dal programma...")  #Termina il programma