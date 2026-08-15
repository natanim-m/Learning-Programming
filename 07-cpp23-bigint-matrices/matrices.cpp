//matrices.cpp
#include <iostream>
#include <vector>
#include <array>
#include <cmath>
#include <cstdint>
#include <bitset>
#include <print>
#include <format>
using namespace std;
constexpr uint64_t BASE = 1000000000ULL;
constexpr long double phi = 1.6180339887498948482L;
struct BigInt {
	vector<uint32_t> chunks;
	BigInt(int num_chunks=1) {
		chunks.resize(num_chunks);
	}
	void set(uint64_t N) {
		chunks.assign(chunks.size(),0);
		for(size_t i = 0; i < chunks.size() && N > 0; i++) {
		chunks[i] = N % BASE;
		N = N / BASE;
		}

	}
	void trim() {
		while(chunks.size() > 1 && chunks.back()==0) {
			chunks.pop_back();
		}
	}
};
BigInt add(const BigInt& A, const BigInt& B) {
	size_t max_size = max(A.chunks.size(), B.chunks.size());
	BigInt result(max_size+1);
	uint64_t carry = 0;
	for (size_t i = 0; i < max_size; i++) {
		uint64_t valA = (i < A.chunks.size()) ? A.chunks[i] : 0;
		uint64_t valB = (i < B.chunks.size()) ? B.chunks[i] : 0;

		uint64_t sum = valA + valB + carry;
		result.chunks[i] = sum % BASE;
		carry = sum / BASE;
	}
	if (carry) {
		result.chunks[max_size]=carry;
	}
	result.trim();
	return result;
}
BigInt multiply(const BigInt& A, const BigInt& B) {
	size_t n = A.chunks.size();
	size_t m = B.chunks.size();
	BigInt result (n+m);
	for (size_t i = 0; i < n; i++) {
		uint64_t carry = 0;
		for (size_t j = 0; j < m; j++) {
			uint64_t total = ((uint64_t)A.chunks[i]*B.chunks[j]) + result.chunks[i+j] + carry;
			result.chunks[i+j] = total % BASE;
			carry = total / BASE;
			}
		size_t l = i + m;
		while (carry > 0 && l < (n + m)) {
			uint64_t total = result.chunks[l] + carry;
			result.chunks[l] = total % BASE;
			carry = total / BASE;
			l++;
			}
		}
	result.trim();
	return result;
}
array<BigInt, 4> matrix_multi(const array<BigInt, 4>& A, const array<BigInt, 4>& B) {
	BigInt topl = add((multiply(A[0],B[0])),(multiply(A[1],B[2])));
	BigInt topr = add((multiply(A[0],B[1])),(multiply(A[1],B[3])));
	BigInt botl = add((multiply(A[2],B[0])),(multiply(A[3],B[2])));
	BigInt botr = add((multiply(A[2],B[1])),(multiply(A[3],B[3])));
	array<BigInt,4> product_matrix = {topl,topr,botl,botr};
	return product_matrix;
	}

string subscriptify(int n) {
    const string subscripts[] = {
        "\u2080", "\u2081", "\u2082", "\u2083", "\u2084",
        "\u2085", "\u2086", "\u2087", "\u2088", "\u2089"
    };

    if (n == 0) return subscripts[0];

    string result = "";
    string digits = to_string(n);

    for (char d : digits) {
        result += subscripts[d - '0'];
    }
    return result;
}
int main()
 {
	int64_t n;
	cout << "Which fibonacci number are you trying to calculate?\n";
	cin >> n;
	cout << "\n";
	if (n<=0) {
		cout << "Please enter a positive number!";
		return 0;
	}
	int64_t bin = n - 1;
	vector<bool> bits;
	if (bin == 0) {
		bits.push_back(false);
	} else {
		while (bin > 0) {
			bits.push_back(bin & 1);
			bin >>= 1;
		}
	}
	long long digits = floor(n * log10(phi) - log10(5)/2) + 1;
	int num_chunks = (digits / 9) + 1;
	BigInt one(num_chunks);
	BigInt zero(num_chunks);
	one.set(1);
	zero.set(0);
	array<BigInt,4> magic_matrix = {one,one,one,zero};
	array<BigInt,4> identity_matrix = {one,zero,zero,one};
	for (int i = bits.size()-1; i >=0; i--) {
		identity_matrix = matrix_multi(identity_matrix, identity_matrix);
		if (bits[i]) {
			identity_matrix = matrix_multi(identity_matrix,magic_matrix);
		}
	}
	BigInt fibnum = identity_matrix[0];
	string sub_n = subscriptify(n);
	print("F{} is:\n\n", sub_n);
	int i = static_cast<int>(fibnum.chunks.size()) - 1;
    while (i > 0 && fibnum.chunks[i] == 0) {
        i--;
    }


    print("{}", fibnum.chunks[i]);
    i--;

    for (; i >= 0; i--) {
        print("{:09}", fibnum.chunks[i]);
    }
    println("");
	return 0;
 }
