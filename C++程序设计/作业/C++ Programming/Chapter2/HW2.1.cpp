#include<iostream>
using namespace std;

int main()
{

    double celsius,fahrenheit;
    cout<<"Enter a degree in Celsius:";
    cin>>celsius;
    fahrenheit=(9.0/5)*celsius+32;
    cout<<celsius<<" Celsius is "<<fahrenheit<<" Fahrenheit";
    return 0;
}