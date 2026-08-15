# Base-10⁹ BigInt Matrix Exponentiation Solver

A small program to calculate the $N$th Fibonacci number using binary matrix exponentiation paired with a custom arbitrary-precision (`BigInt`) vector structure in modern C++23.

---

## Overview

Calculating large Fibonacci numbers ($F_n$ where $n > 10^5$) creates two problems I had to solve: $O(N)$ linear iteration time and standard 64-bit integer overflow. This implementation solves both:

1. **Logarithmic Time Complexity:** I replaced $O(N)$ iteration with an $O(\log N)$ binary matrix exponentiation algorithm. This can drastically speed up the algorithm by making the amount of operations scale slower.
2. **Arbitrary Precision:** I created a custom `BigInt` structure storing digits in Base-$10^9$ chunks. This allowed me to manage larger Fibonacci numbers without major concerns.

---

## Math & Algorithms

### 1. Matrix Exponentiation
Instead of calculating terms one by one in a loop, you can express the Fibonacci relation as a 2x2 matrix multiplication:

$$
\begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n
$$

By applying binary exponentiation (repeated squaring) to the matrix, computing $M^n$ takes $O(\log N)$ steps instead of $O(N)$. For $N = 10^9$, that turns a billion loop iterations into roughly 30 matrix operations.

### 2. Base-$10^9$ Vector Chunking
- Storing numbers in Base-$10^9$ allows each vector element to represent 9 decimal digits.
- Base-$10^9$ is optimal because $10^9 < 2^{31}-1$. When adding or multiplying chunks, two Base-$10^9$ digits plus a carry easily fit into a standard 64-bit unsigned integer (`uint64_t`) without any overflow.
- I used modern C++ printing standards to make it clean and straightforward, each chunk (except the lead digit) is formatted with zero-padding to 9 decimal places.

---

## Compilation

Compile using GCC 14+, Clang 16+, or any C++23 compliant (so long as it supports the `<print>` header, trust me I know the pain after spending so long trying to update GCC because I just so happened to be using GCC 13 and it was a massive headache)  compiler with `-O3` optimization enabled:

```bash
g++ -std=c++23 -O3 matrices.cpp -o matrices
./matrices
```
