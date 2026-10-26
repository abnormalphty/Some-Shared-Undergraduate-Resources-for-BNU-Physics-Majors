#include<iostream>
using namespace std;

int main()
{
    int population=312032486;
    int time=5*365*24*60;
    double v;
    v=60*(1.0/7+1.0/45-1.0/13);
    population+=v*time;
    cout<<"P="<<population<<endl;
    return 0;
}