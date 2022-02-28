#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;  //numero di testcase
	double m, c, t, i;
	int n, k;
	int j; // indice per i test case

	double r; //risparmio mensile
	double mt; //tasse da pagare ogni n mesi
	
	int  ris = 0; // ris: numero di mesi necessari
	double tot = 0; //tot: risparmio accumulato 
	
	cin >> tc; //numero di casi da risolvere
	
	for(j=0; j<tc; j++){
		cin >> m; //stipendio mensile
		cin >> c; //spese fisse
		cin >> t; //percentuale di tasse da pagare	
		cin >> n; //ogni quanti mesi devono essere pagate le tasse
		cin >> i; //spese impreviste
		cin >> k; //ogni quanti mesi arrivano le spese impreviste	
		
		mt = m * n * t; //tasse da pagare ogni n mesi
		
		r = m - c;  // stipedio tolte le spese fisse
		
		ris=0;
		tot=0;
		
		while(tot<1000000){
			ris++;
			tot = (ris * (m - c)) - (int(ris/n) *  t * m * n) - (i * int(ris/k));
				
		}

		
		cout << "Case #"<<j+1<<": "<<ris<<endl;
		
	}

}	

