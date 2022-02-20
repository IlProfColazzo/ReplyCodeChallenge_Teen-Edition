#include <iostream>
#include <fstream>
/*
Created by:
  -Kevin Zuccaro
  -Roberto Marzio
  -Edoardo Leone
  -Alberto Corvaglia
*/
using namespace std;

int arraySum(int arr[],int do_ccumenza,int finu_a_doni){
    int s=0;
    for (int x=do_ccumenza;x<finu_a_doni;x++){
        s=s+arr[x];
    }
    return s;
}

int main()
{
    int DIFFICULTY_LIMIT=1000000;
    int bigDataPoints[DIFFICULTY_LIMIT]={2,3};
    int i = 3;
    int j = i;
    int x = 3;
    int k=3;
    int s=0;
    while(i<DIFFICULTY_LIMIT){
        if(i-j==x){
            x++;
            j=i;
            k=x;
        }
        s=bigDataPoints[k-2]+arraySum(bigDataPoints,0,x-2);
        bigDataPoints[i-1]=s;
        k++;
        i++;
    }
    int T=0;
    string line;
    ifstream iFile("dati");
    ofstream oFile("out");
    while (getline (iFile, line)) {
      T++;
      oFile<<"Case #"<<T-1<<": "<<bigDataPoints[stoi(line)-1]<<endl;
    }

    // Close the file
    oFile.close();
    iFile.close();
    return 0;
}
