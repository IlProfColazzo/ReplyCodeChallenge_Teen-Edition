#########################################-ANDREA COLAZZO-################################################
# La mia risoluzione utilizza il seguente algoritmo:                                                    #
# - per ogni tasto premuto                                                                              #
#   salvo:                                                                                              #
#   1) il codice del tasto premuto                                                                      #
#   2) l'indice di riga                                                                                 #
#   3) l'indice di colonna                                                                              #
#   genero tutti i possibili tasti ottenibili dalle righe e colonne salvate fino a questo momento.      #
#   Se il tasto generato non corrisponde a nessun tasto premuto, allora si ha Ghost.                    #
#   Ottimizzazione non implementata: si ha Gost quando il numero di intersezioni                        #
#   len(activeRow) * len(activeCol) sono maggiori al numero di tasti premuti finora len(pressed).       #
#########################################################################################################


def isGhost(activeRow,activeCol,C,pressed):
    for r in activeRow:
        for c in activeCol:
            key = r * C + c
            if key not in pressed:
                return True
    return False


f = open("in.txt","r")
fo = open("out.txt","w")
TC = int(f.readline())
for t in range(TC):
    row = f.readline().strip().split()
    R = int(row[0])
    C = int(row[1])
    N = int(row[2])
    activeRow  = set()
    activeCol  = set()
    pressed = []
    step = 0
    #for each pressed key
    for k in row[3:]:
        step+=1
        pressed.append(int(k)) #save pressed key
        activeRow.add(int(int(k)/C)) #save row of the pressed key
        activeCol.add(int(k)%C ) #save column of the pressed key
        ghost = isGhost(activeRow,activeCol,C,pressed)
        if ghost:
            break
    if not ghost:
        print("Case #"+str(t+1) + ": -1")
        fo.write("Case #"+str(t+1) + ": -1\n")
    else:
        print("Case #" + str(t + 1) + ": " + str(step - 1))
        fo.write("Case #" + str(t + 1) + ": " + str(step - 1) + "\n")

f.close()
fo.close()