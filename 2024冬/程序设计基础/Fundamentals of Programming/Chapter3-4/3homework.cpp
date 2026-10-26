#include<iostream>
using namespace std;

int main()
{
    int FM = 0 , SM = 0 , TM = 0;
    float FP = 20 , SP = 9.5 ,TP = 6.2;
    float total = 0.0;
    cout<<"一等奖人数"<<endl;
    cin>>FM;
    cout<<"二等奖人数"<<endl;
    cin>>SM;
    cout<<"三等奖人数"<<endl;
    cin>>TM;
    total = FM * FP + SM * SP + TM *TP;
    cout<<"总金额"<<total<<endl;
    return 0;
}