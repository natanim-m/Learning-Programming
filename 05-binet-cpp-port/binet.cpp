// compile with C++ 23 or later for full support of 128 bit precision
#include <iostream>
#include <cmath>
#include <string>
using namespace std;
int main() {
	long long n;
	cout << "Which Fibonacci number would you like to calcualate?";
	cin >> n;
	if (n < 0) { cout << "Please enter a positive number!"; return 0; }
	__float128 s5 = 2.23606797749978969640917366873127623Q;
	__float128 phi = (1.0Q+s5)/2.0Q;
	__float128 psi = (1.0Q-s5)/2.0Q;
	
	__float128 fib_raw = (std::pow(phi, (__float128)n) - std::pow(psi, (__float128)n)) / s5;
	unsigned __int128 fibonacci = (unsigned __int128)(fib_raw + 0.5Q);
	// unfortunately cout doesn't natively support the unsigned 128 bit integer type since it's a compiler extension however I'll use a small loop to make it work.
	string result128bit = "";
	unsigned __int128 temp = fibonacci;
	if (temp == 0) { result128bit = "0"; }
	else { 
	while (temp > 0) {
		result128bit = to_string((int)(temp % 10)) + result128bit;
        temp /= 10;
        }
    }
	cout << "The " << n << " fibonacci number is " << result128bit << "\n";
return 0;
}