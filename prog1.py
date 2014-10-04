import sys
from Matrix import Matrix

def exp(mat, n):
    if n == 1:
        return mat
    return exp(mat * mat, n/2)

lines = [line.strip() for line in open(sys.argv[1])]
n = int(lines[0])
k = int(lines[1])
lines.pop(0)
lines.pop(0)

outfile = sys.argv[2]
#initiates new matrix NxN size 
mat = Matrix(n,n)

i = 0
tempArr = []
for x in lines:
    arr = x.split()
    tempArr.append(arr)


mat.makeMatrix(tempArr)

newMat = exp(mat, pow(2,k))

text_file = open(outfile, "w")
text_file.write(str(newMat))
text_file.close()



