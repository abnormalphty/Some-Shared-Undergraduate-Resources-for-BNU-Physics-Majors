#include<iostream>
using namespace std;

int main()
{
    float radius,length;
    const float pi=3.1415926535;
    cout<<"Enter the radius and length of a cylinder:";
    cin>>radius>>length;
    double area,volume;
    area = pi * radius * radius;
    volume = area * length;
    cout<<"The area is "<<area<<endl;
    cout<<"The volume is "<<volume<<endl;
    return 0;
}