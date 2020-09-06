// more pointers
#include <iostream>
using namespace std;

int main()
{
	int firstvalue = 5, secondvalue = 15;
	int* p1, * p2;

	p1 = &firstvalue;  // p1 = address of firstvalue
	p2 = &secondvalue; // p2 = address of secondvalue

	*p1 = 10;          // value pointed to by p1 = 10
	*p2 = *p1;         // value pointed to by p2 = value pointed to by p1 = 10

	p1 = p2;           // p1 = p2 pointer address is copied (p1 don't point anymore on firstvalue)
	*p1 = 20;          // value i n p1 (p2) = 20, as bot pointer point to secondvalue, firstvalue is not changed

	cout << "firstvalue is " << firstvalue << '\n';
	cout << "secondvalue is " << secondvalue << '\n';
	return 0;
}

