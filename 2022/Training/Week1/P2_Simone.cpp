/* Big data
Componenti squadra: Simone Filippo
                    Bianco Giuseppe
                    Coricciati Giada
                    Romano Roberto
                    Pierri Alessio
 */

#include <iostream>
#include <vector>
using namespace std;
vector<int> v;

void riduci(int num){     //funzione che riduce ogni numero tipo 1+2+3+...+[n-(1+2+3+...)]
  int s=0,c=0,s1,nU=0;    //somma,contatore,somma precedente,ultimo numero
  do{                     //ciclo che elabora quale somma di interi consecutivi è più vicina (sforando) al nostro numero 
    c++;                  
    s1=s;
    s+=c;
  }while(s<num);          //esce sia quando la somma è maggiore che uguale al numero 
  if(s!=num){             //se è uguale questo calcolo non è necessario
    c--;                  //decrementa il contatore perchè ha sforato
    nU=c+(num-s1);        //l'ultimo numero è uguale alla somma dell'ultimo numero consecutivo e quello che è rimasto
    c--;                  //decrementa perché abbiamo tolto l'ultimo numero
  }
  
  for(int i=1;i<=c;i++){  
    v.push_back(i);       //inserisce i numeri consecutivi in un vettore
    }
  if (nU!=0)              
  v.push_back(nU);        //inserisce l'ultimo numero se non è 0
}



int main() {
  freopen("input.txt","r",stdin);       //lettura da file
  freopen("output.txt","w",stdout);
  int N,c,num;                          //numero di input,costo (output),numero da ridurre
  cin>>N;
  for(int i=0;i<N;i++){
  v.clear();                            //svuota il vettore a ogni ciclo
  c=0;                                  //inizializza il costo a 0 a ogni ciclo
  cin>>num;
  riduci(num);
  for(int i=0;i<v.size();i++){          
    if(v[i]!=1&&v[i]!=2){               //riduce tutti i numeri che non siano 1 o 2
      riduci(v[i]);
    }
    if(v[i]==1) c+=2;                   //per ogni 1 aggiunge 2 all'output
    else if(v[i]==2) c+=3;              //per ogni 2 aggiunge 3 all'output
  }
  cout<<"Case #"<<i+1<<": "<<c<<endl;
  }
}