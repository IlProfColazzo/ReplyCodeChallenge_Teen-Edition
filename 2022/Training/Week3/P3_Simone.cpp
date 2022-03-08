#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<int>A,B;
int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T;
  cin>>T;
  for(int i=0;i<T;i++){
    long long N,K,max=0,min=0,maxn,cmax;
    A.clear();
    B.clear();
    cin>>N>>K;
    A.resize(N);
    B.resize(N);
    for(int j=0;j<N;j++){
      cin>>A[j];
      //cout<<A[j]<<" ";
    }
    //cout<<endl;
    for(int j=0;j<N;j++){
      cin>>B[j];
      //cout<<B[j]<<" ";
    }
    //cout<<endl;
    sort(A.begin(),A.end()); //ordina i vettori
    sort(B.begin(),B.end());
    int a=N-1;//punta all'ultimo elemento
    int c=0;
    for(int j=0;j<K;j++){
      cmax=A[a]*B[a];//calcola il prodotto tra gli elementi dei vettori partendo da destra 
      maxn=A[c]*B[c];//stesso procedimento ma partendo da sinistra
      if(cmax>maxn) { //vede qual è il maggiore e lo somma all'accumulatore
        max+=cmax;
        a--;
      }
      else {
        max+=maxn;
        c++;
      }
      //cout<<max<<endl;
      //cout<<A[a]<<" "<<B[a]<<endl<<max<<endl;
    }
    int b=N-1,d=N-1; a=0; c=0; //quattro contatori due per puntare l'inizio di ogni vettore e due per puntare la fine
    for(int j=0;j<K;j++){
      if((A[a]*B[b])<=(A[d]*B[c])){ //calcola il prodotto tra il primo del primo e l'ultimo del secondo e lo confronta con il "contrario"
        min+=A[a]*B[b];
        a++; b--;
      } else {
        min+=A[d]*B[c];
        c++; d--;
      }
    }
    cout<<"Case #"<<i+1<<": "<<min<<" "<<max<<endl;
  }
}