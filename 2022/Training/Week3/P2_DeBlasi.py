# Per trovare la sedia dove ci troveremo dopo k giorni saltiamo 
# da sedia a sedia finché non ci troviamo su una sedia dove siamo già stati, 
# allora troviamo la sedia finale con K modulo (dimensione del loop)

fi = open("input.txt")

T = int(fi.readline())

fo = open("output.txt", "w")

def findFinalSeat(current_seat):
    seat_history = []
    for i in range(0, N):
        if current_seat not in seat_history:
            seat_history.append(current_seat) # qua mettiamo ogni sedia dove siamo stati
            current_seat = seats[current_seat] # ci spostiamo alla sedia successiva
        else:   
            # siamo tornati a una sedia dove siamo già stati: 
            # questo è l'inizio del loop e 
            # l'ultima sedia aggiunta è la fine del loop
            seat_history = seat_history[seat_history.index(current_seat) :]
            return seat_history[(K % len(seat_history))] 
            # con K % (lunghezza del loop) vediamo in che sedia ci troviamo
            # alla fine dei K giorni

    return seat_history[-1] # se non c'è un loop la sieda finale è l'ultima

for k in range(0, T):
    N, K = [int(n) for n in fi.readline().split()]
    seats = [int(n) for n in fi.readline().split()]
    final_seats = [None] * (N)

    for j in range(0, N):
        final_seats[findFinalSeat(j)] = j 

    output = " ".join([str(n) for n in final_seats])
    fo.write(f"Case #{k + 1}: {output}\n")
    #print(output)

print("DONE")

fo.close()

     