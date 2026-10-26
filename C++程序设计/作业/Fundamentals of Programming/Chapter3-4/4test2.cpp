#include<iostream>
using namespace std;

int main()
{
    for (int k=1;k<=4;k++)
    {
        int sum=0;
        if (k!=1)
        {
            sum=sum+1;
        }
        if (k==3)
        {
            sum=sum+1;
        }
        if (k==4)
        {
            sum=sum+1;
        }
        if (k!=4)
        {
            sum=sum+1;
        }
        if (sum==3)
        {
            cout<<"第"<<k<<"个人做了好事"<<endl;
        }
    }
    return 0;
}