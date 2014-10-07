import sys
from Matrix import Matrix
import math 
'''
This is the function for elimination without optimization. O(n^3) time 

def eliminate(A):
	n = A.getRow()
	L = Matrix(n,n)
	U = Matrix(n,n)
	for k in range(0, n):
		if math.fabs(A[k][k]) == 0:
			raise error("fail")
		L[k][k] = 1
		for i in range(k+1, n):
			L[i][k] = A[i][k]/A[k][k]
			for j in range(k+1, n):
				A[i][j] = A[i][j]-(L[i][k] * A[k][j])
		for j in range(k,n):
			U[k][j] = A[k][j]

	return L, U


'''

#this is the function for elimination with optimization. O(n^2*m) where m is m-diagonal matrix
def eliminateOptimized(A, m):
	n = A.getRow()
	L = Matrix(n,n)
	U = Matrix(n,n)
	for k in range(0, n):
		#does not perform row swaps. if the pivot is 0, fail 
		if math.fabs(A[k][k]) == 0:
			raise error("fail")
		#diagonal of L is 1
		L[k][k] = 1
		#sets the width to calculate to m (unless we are near the end of the matrix)
		#then it calculates to n 
		q = n - k + 1 
		if q > m:
			last = k+m
		else:
			last = n
		for i in range(k+1, last):
			L[i][k] = A[i][k]/A[k][k]
			c = L[i][k]
			for j in range(k+1, last):		
				A[i][j] = A[i][j]-(L[i][k] * A[k][j])
		for j in range(k,last):
			U[k][j] = A[k][j]
			'''
	for y in range(n-1, 0-1, -1):
		c = mat[y][y]
		for y2 in range(0,y):
			for x in range(n-1, y-1, -1):
				mat[y2][x] -= mat[y][x] *mat[y2][y]/c

		mat[y][y] /= c
		for x in range(n, n):
			mat[y][x] /= c
	print mat 
'''

	return L, U
'''
def solve(A,b):
	for y in range(h-1, 0-1, -1): 
	L = Matrix(n,n)
	U = Matrix(n,n)
	L,U = eliminateOptimized(A)
	s = 0
	for k in range(1,n):
		for j in range(1,k-1):
'''

def solve(A, b, m):
	#solve Ax=b using L and U from eliminate(A)
	L, U = eliminateOptimized(A, m)
	n = A.getRow()
	c = [0 for x in range(n)]
	x = [0 for x in range(n)]
	s = 0
	t = 0
	first = 0
	for k in range(0, n):
		#optimization: only calculate to the width of the diagonal. 
		#unless at the end, then calculate to n
		if k  < m :
			first = 0 
		else:
			first = k-m
		for j in range(first, k):
			s += L[k][j] * c[j]
		c[k] = (b[k] - s)/L[k][k]
		s = 0
	for k in range(n-1, -1, -1):
		t = 0
		if n-1-k< m :
			last = n-1 
		else:
			last = k+m
		for j in range(last, k, -1):
			
			t = t + U[k][j] * x[j]
		x[k] = (c[k]-t)/(U[k][k])
	return x 


	
lines = [line.strip() for line in open(sys.argv[1])]
n = int(lines[0])
m = int(lines[1])
b = []
for i in lines[2].strip().split():
	b.append(int(i))

lines.pop(0)
lines.pop(0)
lines.pop(0)

outfile = sys.argv[2]

mat = Matrix(n,n)
temp = Matrix(n,n)

i = 0
tempArr = []
for x in lines:
	arr = x.strip().split()
	tempArr.append(arr)

mat.makeMatrix(tempArr)
temp.makeMatrix(tempArr)

'''
L = Matrix(n,n)
U = Matrix(n,n)

L,U = eliminateOptimized(mat, m)
L1,U1 = eliminate(temp)
print L
'''
x = solve(mat,b,m)

text_file = open(outfile, "w")
text_file.write(str(x))
text_file.close()
#print U1
