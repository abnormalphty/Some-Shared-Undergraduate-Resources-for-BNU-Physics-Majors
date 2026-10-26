#include<iostream>
#include<cmath>
using namespace std;

double Pi(int n);

int main()
{
    cout<<Pi(6)<<endl;
    cout<<Pi(7)<<endl;
    return 0;
}

double Pi(int n)
{
    double pi;
    for (int i=1;i<=n;i++)
    {
        pi+=pow(-1,i+1)/(2*i-1);
    }
    pi*=4;
    return pi;
}