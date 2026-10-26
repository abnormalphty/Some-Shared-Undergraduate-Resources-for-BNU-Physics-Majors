#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    int m,n;
    int a[4];
    
    int max,min;
    cout<<"n="<<endl;
    cin>>n;
    if (!(1000<=n<=9999))
    {
        cout<<"hmp，叫你输四位数"<<endl;
    }
    else
    {
        do
        {
            a[0]=n/1000;
            a[1]=(n-1000*a[0])/100;
            a[2]=(n-1000*a[0]-100*a[1])/10;
            a[3]=n-1000*a[0]-100*a[1]-10*a[2];
            sort(a,a+5);
            max=1000*a[3]+100*a[2]+10*a[1]+a[0];
            min=1000*a[0]+100*a[1]+10*a[2]+a[3];
            int detla;
            detla=max-min;
            cout<<detla<<endl;
            m=n;
            n=detla;
        } while (m!=n);
    }
    return 0;
}
