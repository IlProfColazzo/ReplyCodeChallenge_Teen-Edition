/*	Scala Pierpaolo, Fabio Tarì, Salvatore Chiovaro

La nostra soluzione prevede il calcolo del danno che uno infligge all'altro (danno1 e danno2) 
e successivamente del numero di round che ogni giocatore riesce a giocare
*/
#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("i.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int N,L1,A1,D1,L2,A2,D2,danno1,danno2,vincitore,r1,r2;
	cin >> N;
		for(int i=0;i<N;i++){
		cin >> L1;
		cin >> A1;
		cin >> D1;
		cin >> L2;
		cin >> A2;
		cin >> D2;
		danno1 = A1-D2; // individuo il danno "netto" che giocatore1 infligge a giocatore2
		danno2 = A2-D1; // individuo il danno "netto" che giocatore2 infligge a giocatore1
		if(danno1<=0 && danno2<=0){
			vincitore = 0;
		}else if(danno2<=0){
			vincitore = 1;
		}else if(danno1<=0){
			vincitore = 2;
		}else{
			r1=L1/danno2; // round disputati da giocatore1
			r2=L2/danno1; // round disputati da giocatore2
			if(r1>r2){
				vincitore = 1;
			}else if(r2>r1){
				vincitore = 2;
			}else{
				vincitore = 0;
			}
		}

		cout << "Case #" << i+1 << ": " << vincitore << endl; 
	}
	
	
	
	
	return 0;
}
