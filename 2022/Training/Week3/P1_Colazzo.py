#########################################-ANDREA COLAZZO-################################################
# La mia risoluzione utilizza il seguente algoritmo:                                                    #
# - trovo il numero minimo di pezzi                                                                     #
# - provo a generare nkit che parte da 2 al numero trovato precedentemente                              #
#   - riesco a generare un kit se tutti i gadgets hanno una quantità multipla di nkit                   #
#########################################################################################################


f = open("in.txt","r")
fo = open("out.txt","w")
TC = int(f.readline())

for t in range(TC):
    N = map(int,f.readline().strip().split())
    G = [int(i) for i in f.readline().strip().split()]
    k = 1
    minG = min(G)
    for nkit in range(2,minG+1):
        possible = True
        for g in G:
            if g%nkit!=0:
                possible = False
                break
        if possible:
            k+=1
    print("Case #" + str(t + 1) + ": "+str(k))
    fo.write("Case #" + str(t + 1) + ": " + str(k) + "\n")
f.close()
fo.close()