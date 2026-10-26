#include<iostream>
using namespace std;

int n;
int k;
int SOP(int m,int l);
int power(int p,int q);

int main()
{
    cout<<"n="<<endl;
    cin>>n;
    cout<<"k="<<endl;
    cin>>k;
    int result;
    result=SOP(n,k);
    cout<<result<<endl;
    return 0;
}

int SOP(int m,int l)
{
    int sum=0;
    for (int i=1;i<=m;i++)
    {
        sum=sum+power(i,l);
    }
    return sum;
}

int power(int p,int q)
{
    int pro=1;
    for (int j=1;j<=q;j++)
    {
        pro=pro*p;
    }
    return pro;
}