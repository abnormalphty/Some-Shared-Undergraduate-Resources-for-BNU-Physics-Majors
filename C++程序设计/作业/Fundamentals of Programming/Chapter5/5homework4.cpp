#include<iostream>
using namespace std;

int main()
{
    for (int i=7;i<=9;i++)
        for (int j=7;j<=9;j++)
            for (int k=7;k<=9;k++)
            {
                if (i!=j&&i!=k&&j!=k)
                {
                    int num;
                    num=100*i+10*j+k;
                    cout<<num<<endl;
                }
            }
    return 0;
}