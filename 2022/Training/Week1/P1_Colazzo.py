#########################################-ANDREA COLAZZO-################################################
# La mia risoluzione prevede il calcolo, a priori, del costo di tutti i problemi possibili.             #
# Il costo viene memorizzato all'interno di una mappa con chiave la difficoltà e valore il costo.       #
# Al posto delle mappe si potrebbero utilizzare  degli array dove l'indice rappresenta la difficoltà    #
# e il valore il costo.                                                                                 #
# Per calcolare in anticipo il costo di tutti i problemi  ho sfruttato la seguente osservazione.        #
# Costo P1 = 2                                                                                          #
# Costo P2 = 3                                                                                          #
# Costo P3 = Costo P1 + Costo P2                                                                        #
# Costo P4 = Costo P1 + Costo P3                                                                        #
# Costo P5 = Costo P1 + Costo P4                                                                        #
# Costo P6 = Costo P1 + Costo P2 + Costo P3                                                             #
# Costo P7 = Costo P1 + Costo P2 + Costo P4                                                             #
# Costo P8 = Costo P1 + Costo P2 + Costo P5                                                             #
# Costo P9 = Costo P1 + Costo P2 + Costo P6                                                             #
# Costo P10 = Costo P1 + Costo P2 + Costo P3 + Costo P4                                                 #
# Costo P11 = Costo P1 + Costo P2 + Costo P3 + Costo P5                                                 #
# Costo P12 = Costo P1 + Costo P2 + Costo P3 + Costo P6                                                 #
# Costo P13 = Costo P1 + Costo P2 + Costo P3 + Costo P7                                                 #
# Costo P14 = Costo P1 + Costo P2 + Costo P3 + Costo P8                                                 #
# .... e così via....                                                                                   #
# Si può vedere come nelle somme ci sia sempre una parte fissa che si ripete per n iterazioni           #
# dove n parte da 3 e viene incrementanta man mano.                                                     #
#########################################################################################################

mappa = {} #mappa che conterrà il costo totale di ogni singolo problema (da D=1 a D=1000000)
#Key=difficolta value=costo
mappa[1] = 2
mappa[2] = 3

score = {} #mappà che conterrà la parte di somma fissa nelle varie sommatorie
score[1] = 2
i = 3
z = 0
while i <= 1000000:
    z = z + 1
    sommap = score[z]
    for j in range(z+2):
        mappa[i + j] = sommap + mappa[j + z + 1]
    score[z+1] = mappa[i]
    i = i + z + 2
#print(mappa)

f = open("i.txt","r")
fo = open("out.txt","w")
T = int(f.readline())
for t in range(T):
    score = int(f.readline())
    print(mappa[score])
    fo.write("Case #"+str(t+1) + ": " + str(mappa[score])+"\n")
f.close()
fo.close()