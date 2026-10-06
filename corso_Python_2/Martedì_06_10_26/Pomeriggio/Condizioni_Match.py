#Condizioni con Match

richiesta = input("Inserisci una richiesta: ")

match richiesta:
    case "start":
        print("Avvio del programma...")
    case "stop":
        print("Arresto del programma...")
    case "pause":
        print("Pausa del programma...")
    case _: #è come l'else e non è obbligatorio ma può sempre andare bene metterlo
        print("Richiesta non valida.")