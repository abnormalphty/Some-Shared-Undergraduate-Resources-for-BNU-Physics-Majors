#include<iostream>
using namespace std;

int main()
{
    int a;
    cout<<"a="<<endl;
    cin>>a;
    do
    {
        if (a%2==1)
        {
            a=3*a+1;
        }
        else
        {
            a=a/2;
        }
        cout<<a<<endl;
    } while (a!=1);
    return 0;
}