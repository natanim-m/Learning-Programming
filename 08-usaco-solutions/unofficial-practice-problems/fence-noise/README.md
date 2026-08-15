# Unofficial USACO Bronze Practice Problem: Fence Noise

### Problem Statement

Farmer John's $N$ cows ($1 \le N \le 100$) are spread out along a long straight fence consisting of up to 100 numbered fence posts (1 through 100).

Each cow $i$ occupies a continuous segment of the fence starting at post $L_i$ and ending at post $R_i$ ($1 \le L_i \le R_i \le 100$). While occupying her segment, cow $i$ produces a constant noise level of $V_i$ ($1 \le V_i \le 1000$). 

Because multiple cows can occupy overlapping fence segments, the total noise at any given fence post is the sum of the noise levels of all cows whose segments cover that post. 

Farmer John is building a residence near the fence and wants to know the **maximum total noise level** experienced at any single fence post so he can soundproof his house appropriately.

---

### Input Format (file `fence.in`)

* The first line contains a single integer $N$: the number of cows.
* The next $N$ lines each contain three space-separated integers, $L_i$, $R_i$, and $V_i$, describing the fence range and noise level produced by cow $i$.

---

### Output Format (file `fence.out`)

* Output a single integer representing the maximum total noise level at any single fence post $j$ ($1 \le j \le 100$).

---

### Sample Input (`fence.in`)

```text
3
2 6 3
4 8 5
1 3 2
```

### Sample Output (`fence.out`)

```text
8
```

---

### Sample Explanation

* **Cow 1** adds noise $3$ to posts $2, 3, 4, 5, 6$.
* **Cow 2** adds noise $5$ to posts $4, 5, 6, 7, 8$.
* **Cow 3** adds noise $2$ to posts $1, 2, 3$.

Evaluating total noise at each fence post:
* Post 1: $2$ (Cow 3)
* Post 2: $2 + 3 = 5$ (Cows 1, 3)
* Post 3: $2 + 3 = 5$ (Cows 1, 3)
* Posts 4, 5, 6: $3 + 5 = 8$ (Cows 1, 2)
* Posts 7, 8: $5$ (Cow 2)

The maximum total noise at any single post is **8** (at posts 4, 5, and 6).
