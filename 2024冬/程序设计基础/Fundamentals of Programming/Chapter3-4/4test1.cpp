#include<iostream>
using namespace std;

int main()
{
    double e=1.0,c;
    long k=1;
    do
    {
        c=1.0;
        for (int i=1;i<=k;i++)
        {
            c=c/i;
        }
        k++;
        e=e+c;
    }while(c>1e-100);
    cout<<e;
    return 0;
}