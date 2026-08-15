#matrices.py
import sys
sys.set_int_max_str_digits(100000000000)
n = int(input("Which fibonacci number do you want to calculate\n"))
if n <= 0:
    print("Please enter a positive number!")
    exit()
N = n-1
magic_matrix = [
    [1, 1],
    [1, 0]
]
binN=bin(N)[2:]
Nbin=binN[::-1]
def matrixmulti(a,b):
    topl=((a[0][0]*b[0][0])+(a[0][1]*b[1][0]))
    topr=((a[0][0]*b[0][1])+(a[0][1]*b[1][1]))
    botl=((a[1][0]*b[0][0])+(a[1][1]*b[1][0]))
    botr=((a[1][0]*b[0][1])+(a[1][1]*b[1][1]))
    return [[topl,topr],[botl,botr]]
    
result=[[1,0],[0,1]]
for bit in str(Nbin):

    if bit == '1':
        result=matrixmulti(magic_matrix,result)
    magic_matrix = matrixmulti(magic_matrix, magic_matrix)
print(result[0][0])