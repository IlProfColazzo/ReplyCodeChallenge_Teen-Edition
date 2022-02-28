/*	Pierpaolo Scala, Fabio Tarì

la soluzione di questo esercizio prevede l'iterazione sull'obiettivo finale,
ogni mese aggiungiamo il guadagnno netto e se ci troviamo nel mese in cui bisogna pagare le imposte e/o 
imprevisti vengono scalate dai risparmi
*/

#include <bits/stdc++.h>

using namespace std;

int main(){
	int N;
	long double reddito, spese_fisse,tasse, spesa_imp;
	int mesi_tasse, mesi_spesa_imp;
	long double obiettivo=0;
	int mesi=1;
	long double tasse_pag;
	
	freopen("i.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	cin >> N;
	
	for(int i=0; i<N; i++){
		cin>> reddito;
		cin>> spese_fisse;
		cin>> tasse;
		cin>> mesi_tasse;
		cin>> spesa_imp;
		cin>> mesi_spesa_imp;
		
		do{
			obiettivo+=(reddito-spese_fisse);	// entrate mensili nette
			if(mesi%mesi_tasse==0 && mesi_tasse!=0){ 
				tasse_pag=(reddito*mesi_tasse)*tasse; // formula pagamento tasse
				obiettivo-=tasse_pag;
			}
			
			
			if(mesi%mesi_spesa_imp==0 && mesi_spesa_imp!=0){
				obiettivo-=spesa_imp;
			}
			
			mesi++;
		}while(obiettivo<1000000);
		
		mesi--;
		cout << "Case #" << i+1 << ": " << mesi << endl;
		obiettivo=0;
		mesi=1;
	}
}
