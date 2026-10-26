#include<iostream>
using namespace std;

int pow(int p,int q);
int fuc(int i,int n);

int main()
{
    int n,len;
    cout<<"n="<<endl;
    cin>>n;
    len=pow(2,n-1);
    int max=0;
    for (int i=0;i<len;i++)
    {
        int m=1;
        m=fuc(i,n);
        if (max<m)
        {
            max=m;
        }
    }
    cout<<"最大的M为："<<max<<endl;
    return 0;
}

int pow(int p,int q)
{
    int pro=1;
    for (int i=1;i<=q;i++)
    {
        pro=pro*p;
    }
    return pro;
}

int fuc(int i,int n)
{
     int c=0,m=1,count=0;
        do
        {
            int a=0;
            a=i%2;
            if (a==0)
            {
                c++;
            }
            else
            {
                m=m*(c+1);
                c=0;
            }
            i=(i-a)/2;
            count++;
        } while (i>0);
        m=m*(n-count);
        return m;
}