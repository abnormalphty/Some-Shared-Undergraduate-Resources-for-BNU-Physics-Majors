#include<iostream>
using namespace std;

int main()
{
    int a,b,c,d,e=1;
    for (a=1;a<=5;a++)
        for (b=1;b<=5;b++)
            for (c=1;c<=5;c++)
                for (d=1;d<=5;d++)
                    for (e=1;e<=5;e++)
                        {
                            int sum=0;
                            if (((b==2)&&(a!=3))||((b!=2)&&(a==3))) sum++;
                            if (((b==2)&&(e!=4))||((b!=2)&&(e==4))) sum++;
                            if (((c==1)&&(d!=2))||((c!=1)&&(d==2))) sum++;
                            if (((c==5)&&(d!=3))||((c!=5)&&(d==3))) sum++;
                            if (((e==4)&&(a!=1))||((e!=4)&&(a==1))) sum++;
                            if (sum==5)
                            {
                                if (a!=b&&a!=c&&a!=d&&a!=e&&b!=c&&b!=d&&b!=e&&c!=d&&c!=e&&d!=e)
                                {
                                    cout<<a<<b<<c<<d<<e<<endl;
                                }
                            }
                        }
    return 0;
}