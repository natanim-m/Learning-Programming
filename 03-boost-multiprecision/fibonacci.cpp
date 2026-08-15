#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
using namespace boost::multiprecision;
using namespace std;
int main()
{
	int64_t n;
	cout << "How many fibonacci numbers are you computing?\nInput:\n";
	cin >> n;
	cout << "\n";
	if (n<=0) {
		cout << "Please enter a positive number!";
	}
	else {
		cpp_int a = 0;
		cpp_int b = 1;
		for(int64_t i = 0; i<n; i++) {
			cout << a;
			cout << "\n";
			b += a;
			a = b - a;
		}
	}
	cin.ignore();
	cin.get();
	return 0;
}