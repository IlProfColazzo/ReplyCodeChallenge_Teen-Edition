/* Board game
Componenti squadra: Simone Filippo
                    Bianco Giuseppe
                    Coricciati Giada
                    Romano Roberto
                    Pierri Alessio
*/
#include <iostream>
using namespace std;
int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int N,l1,a1,d1,l2,a2,d2;
  cin>>N;
  for(int i=0;i<N;i++){
  cin>>l1>>a1>>d1>>l2>>a2>>d2;
  int end=3;                              //inizializziamo end (output) a un qualsiasi valore che non sia tra i casi particolari
  while(end==3){                          //finchè non è nessuno di questi due valori                  
    if(a2>=d1) l1-=(a2-d1); else end=1;   //controlla che l'attacco di uno non sia minore della difesa di due (e viceversa nella prossima istruzione) altrimenti assegna la vittora a 1  
    if(a1>=d2) l2-=(a1-d2); else end=2;
    if(a2<=d1&&a1<=d2) end=0;             //controlla che non sia un pareggio in caso l'attacco di entrambi dovesse essere minore della difesa altrui
    if(l1<=0&&l2>=0) end=2;               //controlla se 1 raggiunge vita inferiore a 0 e in tal caso assegna la vittoria a 2 (viceversa nella prossima istruzione)
    if(l2<=0&&l1>=0) end=1;               
    if(l2<=0&&l1<=0) end=0;               //controlla che non sia un pareggio
  }
  cout<<"Case #"<<i+1<<": "<<end<<endl;
  }
}