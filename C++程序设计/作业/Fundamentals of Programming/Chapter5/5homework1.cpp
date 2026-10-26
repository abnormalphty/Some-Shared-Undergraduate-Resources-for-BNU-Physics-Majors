#include<iostream>
using namespace std;

float power(float p,int q);
int factorial(int n);
float sin(float x,float epslion);

int main()
{
    float x;
    float epslion;
    float result;
    cout<<"x="<<endl;
    cin>>x;
    cout<<"epslion="<<endl;
    cin>>epslion;
    result=sin(x,epslion);
    cout<<"sin"<<x<<"="<<result<<endl;
    return 0;
}

float power(float p,int q)
{
    float pro=1.0;
    for (int i=1;i<=q;i++)
    {
        pro=pro*p;
    }
    return pro;
}

int factorial(int n)
{
    int pro=1;
    for (int k=1;k<=n;k++)
    {
        pro=pro*k;
    }
    return pro;
}

float sin(float x,float epslion)
{
    float sum=0.0;
    int k=1,c=0;
    float a=0.0;
    do
    {
        a=(power(-1,c)*power(x,k))/factorial(k);
        sum=sum+a;
        k=k+2;
        c++;
    }while (a>=epslion);
    return sum;
}