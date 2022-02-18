#########################################-ANDREA COLAZZO-################################################
# La mia risoluzione prevede:                                                                           #
# - il calcolo della vita persa da ogni giocatore ad ogni attacco subito                                #
# - il numero di round che riesce ad affrontare ogni giocatore                                          #
# Confrontando questi 4 dati è possibile individuare le situazioni di pareggio e vincita                #
#########################################################################################################

f = open("i.txt","r")
fo = open("out.txt","w")
T = int(f.readline())
for t in range(T):
    (L1, A1, D1, L2, A2, D2) = map(int, f.readline().strip().split())
    perde1 = A2 - D1 #vita persa da player 1
    perde2 = A1 - D2 #vita persa da player 2
    roundP1 = L1 // perde1 #numero di round che riesce ad affrontare il player 1
    roundP2 = L2 // perde2 #numero di round che riesce ad affrontare il player 2
    if (perde1<0 and perde2 <0) or roundP1 == roundP2:
        esito = 0
    elif perde1 < 0 or roundP1 > roundP2:
        esito = 1
    else:
        esito = 2
    print(esito)
    fo.write("Case #"+str(t+1) + ": " + str(esito)+"\n")
f.close()
fo.close()