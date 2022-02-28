/*
GRUPPO DI:
  -Kevin Zuccaro
  -Roberto Marzio
  -Edoardo Leone
  -Alberto Corvaglia

Per vedere se ce ghosting noi prendiamo in considerazione per prima cosa i primi 2 tasti, calcoliamo la colonna e la riga,
se il secondo rispetto al primo si trova in una riga E colonna diversa c'è ghosting, altrimenti andiamo a verificare quale sarà il parametro variabile
se rispetto al primo il secondo cambia sulla riga lei sarà variabile e laltra constante, e viceversa.
Stabilendo quale sarà il parametro variabile, nel momento in cui gli altri tasti cambiano, sulla costante, c'è ghosting.
Se tutti i tasti rispettano questa condizione non c'è Ghosting.
*/
#include <iostream>

using namespace std;

int main()
{
    freopen("data.txt", "r", stdin); //Input file
    freopen("output.txt", "w", stdout); //Output file

    int T; //Test Case
    int R; //Rows
    int C; //Coloumns
    int key=0;

    int found; //Ghosting
    bool k; //Inseriamo 0 se nel Test Case la parte variabile e' la colonna o 1 se e' la riga.

    cin>>T;

    //Iteriamo tutti i TestCase
    for (int tC=0;tC<T;tC++){
        found=0, key=0;
        int first_row, first_col;
        int n_key; //Number of Keys
        cin>>R>>C>>n_key; //Prendiamo i valori dal file di input
        for(int i=0;i<n_key;i++){
            cin>>key;
            int row=key/C, col=key%C;
            if(found==0){
            if (i==0){
                first_col=col;
                first_row=row;
            }else if(i==1){
                if (first_col!=col && first_row!=row){
                    found=i;
                    break;
                }else{
                    if (first_col!=col){
                        k=0;
                    }else if (first_row!=row){
                        k=1;
                    }
                }
            }else{
                if (first_col!=col && first_row!=row){
                    found=i;
                }else if(first_col!=col && k==1){
                    found=i;
                }else if(first_row!=row && k==0){
                    found=i;
                }
            }
            }
            }
            cout<<"Case #"<<tC+1<<": ";
            if (found){
                cout<<found<<endl;
            }else{
                cout<<-1<<endl;
            }
        }
        return 0;
    }
