/*Team: Coricciati Giada
	Romano Roberto
	Simone Filippo
	Bianco Giuseppe
	Pierri Alessio
*/

#include<iostream>
using namespace std;
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int i = 0; i < T; i++){
        int R,C,N,g;
        cin >> R; //Numero righe
        cin >> C; //Numero colonne
        cin >> N; //Numero tasti premuti
        int keys[N]; //Tasti premuti
        for(int j = 0; j < N; j++){
            cin >> keys[j];
        }
        int rig[R]; //righe premute
        int col[C]; //colonne premute
        for(int j=0; j<N; j++){
            bool ghosting=false;
            g=-1; //tasto che crea ghosting
            int r=keys[j]/C; //posizione riga del tasto premuto
            int c=keys[j]%C; //posizione colonna del tasto premuto
            rig[j]=r; //inserimento della riga premuta
            col[j]=c; //inserimento della colonna premuta
            for(int k=0; k<j; k++){
                //Se la riga e la colonna del tasto premuto sono diversi da quelle dei tasti già premuti allora c'è ghosting
                if(r!=rig[k] && c!=col[k]){
                    ghosting=true;
                    g=j;
                    break;
                }
            }
            if(ghosting){
                break;
            }
        }
        cout<<"Case #"<<i+1<<": "<<g<<endl;
    }
}