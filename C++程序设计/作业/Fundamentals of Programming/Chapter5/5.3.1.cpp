#include<iostream>
using namespace std;

bool checkprime(int n);
bool check4n1(int m);

int main()
{
    int count=0;
    for (int k=2;k<=100;k++)
    {
        if ((checkprime(k))&&(check4n1(k)))
        {
            count++;
        }
    }
    cout<<count<<endl;
    return 0;
}

bool checkprime(int n)
{
    for (int i=2;i<n;i++)
    {
        if (n%i==0)
        {
            return 0;
        }
    }
    return 1;
}

bool check4n1(int m)
{
    if (m%4==1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}