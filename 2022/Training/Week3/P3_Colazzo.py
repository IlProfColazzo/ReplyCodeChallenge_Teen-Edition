f = open("in.txt","r")
fo = open("out.txt","w")
TC = int(f.readline())
for t in range(TC):
    (N, K) = map(int,f.readline().strip().split())
    A = [int(i) for i in f.readline().strip().split()]
    B = [int(i) for i in f.readline().strip().split()]
    A.sort(reverse=True)  # ordino i due vettori in modo crescente
    B.sort(reverse=True)

    #Calcolo del massimo
    place = 0
    iSx = 0
    iDx = len(A)-1
    smax = 0
    while place<K:
        sumSx = A[iSx] * B[iSx]
        sumDx = A[iDx] * B[iDx]
        if(sumSx>=sumDx):
            smax+=sumSx
            iSx+=1
        else:
            smax += sumDx
            iDx -= 1
        place+=1

#todo: il calcolo del minimo ottimo non funziona quando ci sono solo valori positivi.
# è necessario utilizzare quello non ottimo
# cosa succede nell'ottimo se non ci sono abbastanza valori negativi?


    # smin = 0
    # offA = len(A) - 1
    # offB = len(B) - K
    # for i in range(K):
    #     smin = smin + A[offA - i] * B[offB + i]  # il minimo lo calcolo come la somma dei prodotti tra
    #     # il valore più piccolo in A e il più grande tra i più piccoli del vettore B


    # Calcolo del minimo - ottimo
    smin = 0
    for place in range(K):
        mul1 = A[0] * B[len(B)-1]
        mul2 = A[len(B)-1] * B[0]
        if (mul1 <= mul2):
            smin += mul1
            A.pop(0) #Giocando con gli indici potrei rimuovere le pop
            B.pop(len(B) - 1)
        else:
            smin += mul2
            B.pop(0)
            A.pop(len(A) - 1)

    print("Case #" + str(t + 1) + ": " + str(smin) + " " + str(smax))
    fo.write("Case #" + str(t + 1) + ": " + str(smin) + " " + str(smax) + "\n")

f.close()
fo.close()