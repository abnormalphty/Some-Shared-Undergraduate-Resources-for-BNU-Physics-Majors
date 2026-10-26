#include<iostream>
#pragma once
using namespace std;

int main()
{
	int akey = 0, b = 0;
	int* p = NULL, * q = NULL;
	akey = 66;
	p = &akey;
	q = &b;
	*q = *p;
	cout << "b=" << b << endl;
	cout << "*q=" << *q << endl;
	return 0;
}