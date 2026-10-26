#include<iostream>
using namespace std;

int main()
{
    float x=0.0;
    cout<<"请输入待求绝对值的值"<<endl;
    cin>>x;
    if (x>=0)
    {
        cout<<"|x|="<<x<<endl;
    }
    else
    {
        x=-x;
        cout<<"|x|="<<x<<endl;
    }
    return 0;
}