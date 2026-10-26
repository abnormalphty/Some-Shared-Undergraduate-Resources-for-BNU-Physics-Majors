#include<iostream>
using namespace std;


int main()
{
    
    for (int i=1;i<=4;i++)
    {
        int sum=0;
        if (i==2) sum++;
        if (i==4) sum++;
        if (i!=3) sum++;
        if (i!=4) sum++;
        if (sum==1)
        {
            cout<<"最佳车为"<<i<<"号车"<<endl;
        }

    }
    return 0;
}