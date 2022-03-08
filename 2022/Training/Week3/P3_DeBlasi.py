# Per gli ultimi input

# Per il min moltiplichiamo un valore più basso con un valore più alto 
# scegliamo da che lista prendere il più basso e il più alto calcolando entrambi e 
# selezionando il più basso

# Per il max facciamo la stessa cosa ma con valori o entrambi bassi o entrambi alti
# tutto questo perchè vi sono presenti valori negativi.

fi = open("input.txt")

T = int(fi.readline())

fo = open("output.txt", "w")

for k in range(0, T):
    N, K = [int(n) for n in fi.readline().split()]
    buildings = sorted([int(n) for n in fi.readline().split()])
    antennas = sorted([int(n) for n in fi.readline().split()])

    min = 0
    max = 0

    j = 1
    l = 1
    
    for i in range (0, K):
        temp1 = (buildings[j - 1] * antennas[-j])
        temp2 = (buildings[-l] * antennas[l - 1])

        if temp1 <= temp2:
            j = j + 1
            min = min + temp1
        elif temp2 < temp1:
            l = l + 1
            min = min + temp2

    j = 1
    l = 1
    for i in range (0, K):
        temp1 = (buildings[j - 1] * antennas[j - 1])
        temp2 = (buildings[-l] * antennas[-l])

        if temp1 >= temp2:
            j = j + 1
            max = max + temp1
        elif temp2 > temp1:
            l = l + 1
            max = max + temp2

    fo.write(f"Case #{k + 1}: {min} {max}\n")

print("DONE")

fo.close()


# Soluzione per i primi input, nel while(False) perchè python non ha multi line comments
while(False):

    # Funziona solo con i primi input
    # Per il min moltiplichiamo i valori più bassi incrociati 
    # Per il max moltiplichiamo i valori più alti tra di loro in ordine decrescente

    fi = open("input.txt")

    T = int(fi.readline())

    fo = open("output.txt", "w")

    for k in range(0, T):
        N, K = [int(n) for n in fi.readline().split()]
        buildings = sorted([int(n) for n in fi.readline().split()])
        antennas = sorted([int(n) for n in fi.readline().split()])

        min = 0
        max = 0
        j = K
        for i in range (0, K):
            j = j - 1
            min = min + buildings[i] * antennas[j]


        for i in range (1, K + 1):
            max = max + buildings[-i] * antennas[-i]


        fo.write(f"Case #{k + 1}: {min} {max}\n")

    print("DONE")

    fo.close()
