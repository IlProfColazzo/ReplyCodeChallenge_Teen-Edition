#Apre il file di input
fi = open("input.txt")

#Legge il numero di scontri
T = int(fi.readline())

#Apre il file di output
fo = open("output.txt", "w")

#Viene eseguito per ogni scontro
for i in range(0, T):
    #Legge la riga delle statistiche di ogni scontro
    stats = fi.readline().split()
    
    #Non necessario
    L1 = int(stats[0])
    A1 = int(stats[1])
    D1 = int(stats[2])
    L2 = int(stats[3])
    A2 = int(stats[4])
    D2 = int(stats[5])
    
    #Calcola l'attacco effettivo
    A1 = A1 - D2
    A2 = A2 - D1
    
    #Simula lo scontro
    while (L1 > 0 and L2 > 0):
        #Se l'attacco è meno di 0 per entrambi l'esito è pareggio
        if (A1 <= 0 and A2 <= 0):
            L1 = 0
            L2 = 0
        if  (A2 > 0):
            L1 = L1 - A2
        if  (A1 > 0):
            L2 = L2 - A1


    #Se entrambi i giocatori hanno meno di 1 L è pareggio
    if (L1 < 1 and L2 < 1):
        result = "Case #" + str(i+1) + ": 0"
    #Altrimenti il giocatore con L > 0 vince
    elif (L2 < 1):
        result = "Case #" + str(i+1) + ": 1"
    elif (L1 < 1):
        result = "Case #" + str(i+1) + ": 2"
        
    #Scrive il risultato su output
    fo.write(result)
    print(result)