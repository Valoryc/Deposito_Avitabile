def mod_scrittura():
    #Valorizzazione pseudo oggetto dal file
    File_prova_da_open = open ("corso_Python_11/Lunedi_19_10_26/Mattina/I/prova.txt", "r") #pseudo oggetto

    #lettura totale del file
    contenuto_file_tot= File_prova_da_open.read()

    print(contenuto_file_tot)

    #lettura riga per riga
    contenuto_file_riga= File_prova_da_open.readline()

    print(contenuto_file_riga)

    File_prova_da_open.close()

File_prova_da_open = open ("corso_Python_11/Lunedi_19_10_26/Mattina/I/prova.txt", "w")
File_prova_da_open.write("pIPpa")

with open("corso_Python_11/Lunedi_19_10_26/Mattina/I/prova.txt", "r") as file:
        contenuto=File_prova_da_open.read()
