# Fibonacci Solver via Binets formula
import math
phi=(1 + math.sqrt(5)) / 2
psi=(1 - math.sqrt(5)) / 2
n=int(input("Which Fibonacci number are you attempting to calculate?\n"))
def binet(n):
    fibonacci=(phi**n-psi**n)/math.sqrt(5)
    return round(fibonacci)

print(f"The {n} Fibonacci number is {binet(n)}")