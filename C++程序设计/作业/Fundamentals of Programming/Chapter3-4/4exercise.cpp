#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    int x=0,y=0,k=0,a=0,b=0;
    cout<<"x="<<endl;
    cin>>x;
    cout<<"y="<<endl;
    cin>>y;
    k=max(x,y);
    do
    {
        k++;
        a=k%x;
        b=k%y;
    }while (!((a==0)&&(b==0)));
    cout<<k<<endl;
    return 0;
}