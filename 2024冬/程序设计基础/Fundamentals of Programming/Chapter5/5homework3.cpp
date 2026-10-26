#include<iostream>
using namespace std;

int main()
{
    for (int i=0;i<=10;i++)
        for (int j=0;j<=5;j++)
            for (int k=0;k<=2;k++)
            {
                float money=0.0;
                money=0.1*i+0.2*j+0.5*k;
                if (money==1)
                {
                    cout<<i<<"  "<<j<<"  "<<k<<endl;
                }
            }
    return 0;
}