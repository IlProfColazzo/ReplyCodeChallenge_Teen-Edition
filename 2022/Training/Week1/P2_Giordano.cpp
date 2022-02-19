#include <bits/stdc++.h>

using namespace std;

int risolvi_equazione(int);

void calcola(int);

vector <int> v;
vector <int> r;
int  j, h;
long long t;
long long d;
long long n;
long long ultimo = 0;
long long check, diff;
long long costo=0;	


int main(){
	int i;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	costo=0;
	v.push_back(0);
	v.push_back(2);
	v.push_back(3);

	for(i=3;i<1000001;i++){
		r.clear();
		calcola(i);
		costo=0;
		for(j=0;j<r.size();j++)
		{
			costo += v[r[j]];
		}
		v.push_back(costo); 
	/*	for(h=0;h<v.size();h++){
			cout << v[h] << " ";
		}*/
	}
	
	cin >> t; //numero di casi da risolvere
	
	for(i=0; i<t; i++){
		cin >> d; //difficoltà	
		cout << "Case #"<<i+1<<": "<<v[d]<<endl;
	}
	

}	

void calcola(int d){
	long long n;
	int i;
	n = risolvi_equazione(d);
	check = n*(n+1)/2;
	for(i=0;i<=n;i++)
		r.push_back(i);
	if(check!=d){
		ultimo =d - check;
		if(ultimo <= n){
			ultimo += n;
			r.pop_back();
			r.push_back(ultimo);
		}
	}
	/*for(i=0;i<=n;i++){
		cout << "r: "<<r[i]<<" "<<endl;
	}*/
}

int risolvi_equazione(int d){
	long long q=0;
	int delta = 1+(4*(2*d));

    if(delta==0) {
	    q=(-1)/(2*1);
 	}
    else
   	{
	    q=(-1+sqrt(delta))/(2*1);
  	}
  	return q;
}


