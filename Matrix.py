import sys
class Matrix:
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.arr = [[0 for x in xrange(row)] for x in xrange(col)]
	
	def makeMatrix(self, twod_list):
		for i in xrange(len(twod_list)):
			for j in xrange(len(twod_list[i])):
				self.arr[i][j] = 2 

	def at(self, i,j):
		return self.arr[i][j]
		
	def printMatrix(self):
		stri = ""
		for i in xrange(len(self.arr)):
			if i is not 0:
				stri += "\n"
			for j in xrange(len(self.arr[i])):
				stri += str(self.arr[i][j]) + " "
		print stri

test = [[1,2],[3,5]]
newM = Matrix(2,2)
newM.makeMatrix([[2,3],[2,2]])
newM.printMatrix()
print newM.at(1,1)


				
