#include<iostream>
using namespace std;

int main()
{
    int sum=1;
    int n;
    cin>>n;
    for (int k=1;k<=n;k++)
    {
        sum=sum*k;
    }
    cout<<n<<"!="<<sum<<endl;
    return 0;
}