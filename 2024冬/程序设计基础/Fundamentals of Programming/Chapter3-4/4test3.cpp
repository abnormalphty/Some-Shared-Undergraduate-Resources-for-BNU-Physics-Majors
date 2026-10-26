#include<iostream>
using namespace std;

int main()
{
    int cc1,cc2,cc3,cc4,cc5,cc6;
    for (int A=0;A<=1;A++)
        for (int B=0;B<=1;B++)
            for (int C=0;C<=1;C++)
                for (int D=0;D<=1;D++)
                    for (int E=0;E<=1;E++)
                        for (int F=0;F<=1;F++)
                        {
                            cc1=A||B;
                            cc2=!(A&&D);
                            cc3=(A&&E)||(A&&F)||(E&&F);
                            cc4=(B&C)||(!B&!C);
                            cc5=(C&&!D)||(D&&!C);
                            cc6=D||(!D&&!E);
                            if (cc1+cc2+cc3+cc4+cc5+cc6==6)
                            {
                                cout<<A<<B<<C<<D<<E<<F<<endl;
                            }
                        }
    return 0;
}