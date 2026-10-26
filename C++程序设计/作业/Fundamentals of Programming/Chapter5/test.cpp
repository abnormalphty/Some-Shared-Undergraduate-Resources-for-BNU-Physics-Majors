#include <iostream> 
using namespace std;

int pow(int p,int q);

int main()
{
    int n,len;
    cin>>n;
    len=pow(2,n-1);
    int max=0;
    for (int i=0;i<len;i++)
    {
        cout<<"循环for"<<endl;
        int c=0,m=1,count=0;
        do
        {
            cout<<"循环do...while..."<<endl;
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

    }
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