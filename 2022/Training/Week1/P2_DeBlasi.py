#Funzione che calcola e restituisce il costo di un problema con difficoltà D
def calcola(D):
    total = 0 #Difficoltà totale della sequenza
    currentN = 0 #Numero attuale da aggiungere alla sequenza
    totalCost = 0 #Costo totale (viene restituito alla fine)
    
    #Se la difficoltà è 1 o 2 restituisce direttamente il costo adeguato
    if (D == 1):
        return 2
    elif (D == 2):
        return 3
    else:
        #Se la difficoltà è maggiore inizia il calcolo di numeri sequenziali
        # utilizzando currentN per tenere traccia del numero da aggiungere
        while total < D:
            if(total + currentN == D):
                total = total + currentN
                #Per ogni numero aggiunto alla sequenza si chiama la funziona calcola
                # e si aggiunge il risultato al costo totale
                totalCost = totalCost + calcola(currentN)
            else:
                #Se il totale + il numero corrente + il numero successivo supera D
                # bisogna trovare il successivo (non consecutivo)
                # che se aggiunto al totale raggiunge D
                if (total + currentN + currentN + 1 > D):
                    if (total + currentN + 1 == D):
                        currentN = currentN + 1
                        total = total + currentN
                        totalCost = totalCost + calcola(currentN)
                    else:
                        #Aumenta currentN finchè non si trova quello adatto
                        currentN = currentN + 1
                else:
                    #Se il totale + il numero corrente + il numero successivo
                    # non superano N si prosegue con la sequenza normalmente
                    total = total + currentN
                    totalCost = totalCost + calcola(currentN)
                    currentN = currentN + 1

    #Alla fine delle operazioni restituisce il costo totale
    return totalCost

#Apre il file di input
fi = open("input.txt")

#Legge il numero di problemi da risolvere
T = int(fi.readline())

#Apre il file di output
fo = open("output.txt", "w")

#Viene eseguito per ogni problema
for i in range(0, T):
    
    #Legge la difficoltà D
    D = int(fi.readline())

    #Chiama la funzione calcola con D e salva il risultato
    result = calcola(D)
    
    #Scrive il risultato sul file output
    fo.write("Case #" + str(i + 1) + ": " + str(result) + "\n")
    print(result)

fi.close()
fo.close()
