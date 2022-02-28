#########################################-ANDREA COLAZZO-################################################
# La mia risoluzione prevede:                                                                           #
# - ipotesi K è maggiore di N: nei file forniti sempre valida                                           #                                                                    #
# - calcolo quanto riesco a metter da parte dopo aver pagato gli imprevisti e le tasse --> RafterK      #
# - calcolo quanto riesco a metter da parte fino al mese prima di pagare l'imprevisto   --> RafterKm1   #
# - Risolvo la seguente diseguazione RafterKm1 + RafterK x >=1000000                                    #
# - x mi rappresenta blocchi da K mesi                                                                  #
# - moltiplicando x*K ottengo l'indice di partenza da cui iniziare a fare il brute force                #
#########################################################################################################


f = open("input.txt","r")
fo = open("out.txt","w")
TC = int(f.readline())
for t in range(TC):
    (M, C, T, N, I, K) = map(float, f.readline().strip().split())

    nettoMensione = M - C
    RafterKm1=((K-1) * nettoMensione) - (int((K-1)/N) * T * M * N) - (I * int((K-1)/K))
    #gestione del caso in cui il guadagno lo ottengo prima dell'imprevisto
    if RafterKm1>=1000000:
        x = 0
    else:
        RafterK=(K * nettoMensione) - (int(K/N) * T * M * N) - (I * int(K/K))
        x = (1000000 - RafterKm1) / RafterK

    R = 0
    mesi = int(K * x)
    while R<1000000:
        R = (mesi * nettoMensione) - (int(mesi / N) * T * M * N) - (I * int(mesi / K))
        mesi+=1

    print("Case #" + str(t + 1) + ": " + str(mesi-1))
    fo.write("Case #"+str(t+1) + ": " + str(mesi-1)+"\n")
f.close()
fo.close()