#include <iostream>
#include <vector>
using namespace std;

vector<int>V,vattuale,vprecedente;
int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T,N,G;
  cin>>T;
  for(int i=0;i<T;i++){
    V.clear();
    vattuale.clear();
    cin>>N>>G;
    V.resize(N);
    vattuale.resize(N);
    for(int j=0;j<N;j++){
      cin>>V[j]; //vettore fisso che salva le posizioni
      vattuale[j]=j; //vettore variabile inizializzato con i numeri da 0 a N
    }
    for(int j=1;j<=G;j++){
      vprecedente=vattuale; //salva il vettore in un altro di appoggio prima di modificarlo
      for(int c=0;c<N;c++){
        vattuale[V[c]]=vprecedente[c]; //scambia i posti secondo i numeri memorizzati in V (non saprei spiegarlo meglio però insomma l'avete fatto tutti avete capito no??)
      }
    }
    cout<<"Case #"<<i+1<<":";
    for(int j=0;j<N;j++)
      cout<<" "<<vattuale[j];
    cout<<endl;
  }
}