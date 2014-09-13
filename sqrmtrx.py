import sys
from Matrix import Matrix

def exp(mat, n):
    print " round "
    if n == 1:
        return mat
    return exp(mat * mat, n/2)

lines = [line.strip() for line in open(sys.argv[1])]
n = lines[0]
k = lines[1]
lines.pop(0)
lines.pop(0)

mat = Matrix(n,n)

i = 0
tempArr = []
for x in lines:
    arr = x.split()
    tempArr.append(arr)

mat.makeMatrix(tempArr)

print mat
newMat = exp(mat, pow(2,3))
print newMat



