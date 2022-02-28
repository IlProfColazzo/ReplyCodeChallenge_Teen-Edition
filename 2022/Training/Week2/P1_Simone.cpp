/*Team: Simone Filippo
		Bianco Giuseppe
		Pierri Alessio
		Coricciati Giada
		Romano Roberto*/

#include <iostream>
using namespace std;
const int quota=1000000;
int main() {
double guadagnoMensile,costiGiornalieri,risparmi=0,tassePerc,imprevisti;
  int test,mesi,mesiImprevisti,mesiTasse;
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin>>test;
  for(int i=0;i<test;i++){ 
    cin>>guadagnoMensile>>costiGiornalieri>>tassePerc>>mesiTasse>>imprevisti>>mesiImprevisti;
    mesi=0;
    risparmi=0;
    do{
      mesi++; //aumenta il contatore dei mesi
      risparmi=mesi*(guadagnoMensile-costiGiornalieri); //sottrae la spesa mensile fissa allo stipendio
      risparmi-=(mesi/mesiTasse)*(mesiTasse*guadagnoMensile*tassePerc); //sottrae il prodotto tra il prezzo da pagare per le tasse e il numero di mesi per cui sono state pagate (dato dal rapporto tra i mesi totali e i mesi ogni quanto bisogna pagarle)
      risparmi-=(mesi/mesiImprevisti)*imprevisti; //stesso discorso ma con gli imprevisti
    }while(risparmi<1000000);
    cout<<"Case #"<<i+1<<": "<<mesi<<endl;
  }
}
