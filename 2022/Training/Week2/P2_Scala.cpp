/* Pierpaolo Scala,Salvatore Chiovaro, Fabio Tarì, Salvatore De Fazio

Esaminando gli esempi del pdf abbiamo notato che il ghosting è presente se i tasti non sono ne in riga
ne in colonna, perciò eseguiamo due controlli:
1) se sono in colonna la differenza tra il tasto maggiore e quello minore sarà un multiplo di C
2) per verificare che i tasti siano in riga invece troviamo "l'indice" della riga e lo controlliamo 
con quello del tasto successivo
*/

#include <bits/stdc++.h>
using namespace std;
int main(){
	freopen("i.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int NT=0,G=0,R=0,C=0,N=0,diff=0,riga=0,colonna=0,x=0;
	cin >> NT;

	for(int i=0;i<NT;i++){
		cin>> R;
		cin >> C;
		cin >> N;
		int tasti[N];
		for(int j=0;j<N;j++){
			cin>> tasti[j];
		}
		if(N==1){
			G=-1;
		}else{
			for(int j=1;j<N;j++){

				if(tasti[j-1]>tasti[j]){
					diff = tasti[j-1]-tasti[j];
				}else{
					diff = tasti[j]-tasti[j-1];
				}

				if(diff%C==0){	// controllo se in colonna
					// sono in colonna
                    colonna++;
					G=-1;
				}else {
					// verifica se in riga
					for(x=j;x<N;x++){
						if(((int)tasti[x]/C)== ((int)tasti[x-1]/C)){	// controllo se in riga
							// sono in riga
							riga++;
							G=-1;
							if(colonna!=0 && riga!=0){
                                G=x;
                                break;
							}
						}else{
							G=x;
							break;
						}
					}
					if(G==x){
                        break;
					}
				}
			}
		}
		cout << "Case #" << i+1 << ": " << G << endl;
		for(int j=0;j<N;j++){
			 tasti[j]=0;
		}
		R=0;
		C=0;
		riga=0;
		colonna=0;
		G=0;
		x=0;
	}
	return 0;
}
