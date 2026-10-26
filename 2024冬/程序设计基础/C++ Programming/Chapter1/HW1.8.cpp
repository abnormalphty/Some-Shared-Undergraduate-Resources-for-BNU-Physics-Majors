#include<iostream>
using namespace std;

int main()
{
    cout<<"Enter the R:";
    float R,C,A;
    const double pi=3.1415926535;
    cin>>R;
    C=2*pi*R;
    A=pi*R*R;
    cout<<"C="<<C<<"   A="<<A<<endl;
    return 0;
}