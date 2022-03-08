#########################################-ANDREA COLAZZO-################################################
# La mia risoluzione utilizza il seguente algoritmo:                                                    #
# - utilizzo due vettori: actualSeat e futureSeat e per ogni k aggiorno futureSeat;                     #
# al termine degli shift aggiorno actualSeat con futureSeat                                             #
# Algoritmo lento perchè quadratico, sul quarto file gira al pelo, sul quinto                           #
# non si riesce a stare nei tempi.                                                                      #
# Possibile soluzione: sfruttare una qualche proprietà matematica delle seq.                            #
#########################################################################################################


f = open("inSeat1.txt","r")
fo = open("out.txt","w")
TC = int(f.readline())
for t in range(TC):
    (N, K) = map(int,f.readline().strip().split())
    P = [int(i) for i in f.readline().strip().split()]
    actualSeat = [int(i) for i in range(len(P))]
    futureSeat = [int(i) for i in range(len(P))]

    for k in range(K):
        for i in range(len(actualSeat)):
            futureSeat[P[i]] = actualSeat[i]
        actualSeat = futureSeat.copy()
    out = ""
    for i in actualSeat:
        out = out + str(i) + " "
    print("Case #" + str(t + 1) + ": " + out)
    fo.write("Case #" + str(t + 1) + ": " + out + "\n")

f.close()
fo.close()

