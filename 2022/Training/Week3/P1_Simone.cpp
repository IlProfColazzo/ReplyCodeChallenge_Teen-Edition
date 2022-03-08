//Simone Filippo
//Il numero di combinazioni possibili è uguale al numero di divisori in comune dei valori in input
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
vector<int> V;
int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T,N,div,mcd;
  cin>>T;
  for(int i=0;i<T;i++){
    V.clear();
    cin>>N;
    V.resize(N);
    div=0;
    for(int j=0;j<N;j++)
      cin>>V[j];
    mcd=V[0];
    for(int j=1;j<N;j++)
      mcd=__gcd(V[j],mcd); //calcoliamo in mcd tra tutti i numeri del vettore
    
    for(int j=1;j<=mcd;++j){
      if(mcd%j==0) //i divisori del mcd saranno tutti i divisori in comune dei numeri
        div++; 
    }
      
        
    cout<<"Case #"<<i+1<<": "<<div<<endl;
  }
}