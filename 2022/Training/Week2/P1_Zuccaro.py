#Gruppo di:
# Zuccaro Kevin
# Marzio Roberto
# Corvaglia Alberto
# Leone Edoardo

def get_data(file_name:str):
    with open(file_name,'r') as input_data:
        data=[list(map(float,x.split(" "))) for x in input_data.readlines()[1:]]
        return data



def mesi_a_traguardo(STIPENDIO,SPESE_FISSE,TASSE,PERIOD_TASSE_SPESE,INASPETTATE,PERIOD_INASPETTATE):
    salvadanaio=0
    mesi_lavorati=0
    traguardo=1000000


    while salvadanaio<traguardo: 
        mesi_lavorati+=1;
        salvadanaio+=STIPENDIO-SPESE_FISSE;
        if not (mesi_lavorati%PERIOD_TASSE_SPESE):
            salvadanaio-=STIPENDIO*TASSE*PERIOD_TASSE_SPESE
        if not (mesi_lavorati%PERIOD_INASPETTATE):
            salvadanaio-=INASPETTATE
    
    return mesi_lavorati

if __name__=="__main__":
    I_FILE_NAME="data"
    O_FILE_NAME="out"
    
    file=get_data(I_FILE_NAME)
    r=""
    T=0
    for i in file:
        T+=1
        print(T)
        r+=f"Case #{T}: {mesi_a_traguardo(i[0],i[1],i[2],i[3],i[4],i[5])}\n"
    with open(O_FILE_NAME,"w") as out:
        out.write(r)
