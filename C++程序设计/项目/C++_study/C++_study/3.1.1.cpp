#include<iostream>
#pragma once

using namespace std;

int main()
{
	float applePrice = 3.5;
	float bananaPrice = 4.2;
	float appleWeight = 0.0;
	float bananaWeight = 0.0;
	cout << "Please enter the weight of apple:" << endl;
	cin >> appleWeight;
	cout << "Please enter the weight of banana:" << endl;
	cin >> bananaWeight;
	float total = 0.0;
	total = applePrice * appleWeight + bananaPrice * bananaWeight;
	cout << "You should pay " << total << " yuan." << endl;
	return 0;
}