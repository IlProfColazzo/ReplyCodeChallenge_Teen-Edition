#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long t;
	long long l1, a1, d1, l2, a2, d2;
	long long g1, g2, v1, v2;
	int  i;
	
	cin >> t; //numero di casi da risolvere
	
	for(i=0; i<t; i++){
		cin >> l1; //vita giocatore1
		cin >> a1; //attacco giocatore1
		cin >> d1; //difesa giocatore1	
		cin >> l2; //vita giocatore2
		cin >> a2; //attacco giocatore2
		cin >> d2; //difesa giocatore2			
		
		
		g1=a1-d2;
		g2=a2-d1;
		v1=l1/g2;
		v2=l2/g1;
		
		//cout << "g1: "<<g1 << " - v1: " << v1<< endl;
		//cout << "g2: "<<g2 << " - v2: " << v2<< endl;
		
		if(g2<0 && g1<0)
			cout << "Case #"<<i+1<<": "<<0<<endl;
		else if(g2<0)
			cout << "Case #"<<i+1<<": "<<1<<endl;
		else if(g1<0)
			cout << "Case #"<<i+1<<": "<<2<<endl;
		else if(v1==v2)
			cout << "Case #"<<i+1<<": "<<0<<endl;
		else if(v1<v2)
			cout << "Case #"<<i+1<<": "<<2<<endl;
		else if(v1>v2)
			cout << "Case #"<<i+1<<": "<<1<<endl;
		
	}

}	

