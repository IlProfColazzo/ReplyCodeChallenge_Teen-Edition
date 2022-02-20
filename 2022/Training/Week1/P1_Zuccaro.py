//Created by:
//  Kevin Zuccaro
//  Roberto Marzio
//  Edoardo Leone
//  Alberto Corvaglia

def get_data(file_name:str):
    with open(file_name,'r') as input_data:
        data=[list(map(int,x.split(" "))) for x in input_data.readlines()[1:]]
        return data
    
def board_game(data:list[int]):
    L1=data[0] #Life of first player
    A1=data[1] #Attack of first player
    D1=data[2] #defens of first player
    L2=data[3] #Life of second player
    A2=data[4] #attack of second player
    D2=data[5] #defense of second player
    
    while L1>0 and L2>0:
        #print(L1,A1,D1,L2,A2,D2)
        if A2<=D1 and A1<=D2:
            return 0
        if A2>D1:
            L1-=A2-D1
        if A1>D2:
            L2-=A1-D2
            
    if L1==L2 or (L1<=0 and L2<=0):
        return 0
    elif L1<=0:
        return 2
    elif L2<=0:
        return 1
    else:
        return 'Non ci funonzia'
    
if __name__ == "__main__":
    I_FILE_NAME='dati'
    
    data=get_data(I_FILE_NAME)
    T=0 #Score of case
    for x in data:
        T+=1
        print(f"Case #{T}: {board_game(x)}")
