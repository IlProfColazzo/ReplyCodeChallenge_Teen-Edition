#########################################-ANDREA COLAZZO-################################################
# E' possibile vedere che dopo al massimo N scambi, i posti diventano quelli iniziali.                  #
# Sfruttando questo fatto è possibile costrutire a priori per ogni posto una lista                      #
# degli utenti che si alterneranno su un posto. Al massimo si avrà una lista di dimensioni N*N,         #
# nel caso peggiore 100000*100000                                                                       #
# Esempio per file input: 3 5 1 0 4 8 6 2 7 9                                                            #
# 0->3                                                                                                   #
# 1->5->8->7->2                                                                                          #
# 1->5->8->7->2                                                                                          #
# 2->1->5->8->7                                                                                          #
# 3->0                                                                                                   #
# 4                                                                                                      #
# 5->8->7->2->1                                                                                          #
# 6                                                                                                      #
# 7->2->1->5->8                                                                                          #
# 8->7->2->1->5                                                                                          #
#########################################################################################################


f = open("inSeat5.txt","r")
fo = open("out.txt","w")
TC = int(f.readline())

for t in range(TC):
    (N, K) = map(int,f.readline().strip().split())
    P = [int(i) for i in f.readline().strip().split()]
    listoflist = []
    for i in range(N):
        src = i
        dest = -1
        lista = []
        lista.append(src)
        while(dest!=i):
            dest = P[src]
            if dest!=i:
                lista.append(dest)
                src = dest
        listoflist.append(lista)

    out = ""
    K-=1
    for i in range(N):
        size = len(listoflist[i])
        y = K % size
        #y = j % size
        if (size==1):
            out = out + str(listoflist[i][0]) + " "
        else:
            out = out + str(listoflist[i][size-y-1]) + " "
    print("Case #" + str(t + 1))
    fo.write("Case #" + str(t + 1) + ": " + out + "\n")

f.close()
fo.close()