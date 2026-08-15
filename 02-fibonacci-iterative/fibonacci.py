n = int(input("How many numbers are you computing? "))

if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print([1])
elif n == 2:
    print([1, 1])
else:
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b
