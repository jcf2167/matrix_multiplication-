import sys


class Matrix:
    def __init__(self, row, col):
        row = int(row)
        col = int(col)
        self.row = int(row)
        self.col = int(col)
        self.arr = [[0 for x in xrange(row)] for x in xrange(col)]

    def makeMatrix(self, twod_list):
        for i in xrange(len(twod_list)):
            for j in xrange(len(twod_list[i])):
                self.arr[i][j] = float(twod_list[i][j])

    def __getitem__(self, key):
        return self.arr[key]

    def __setitem__(self, key, arr):
        return self.arr[key]

    def __mul__(self, matrixB):
        # self is n x m
        # matrixB is p x k
        # if matrixB's row # doesn't match self's col #
        if matrixB.row is not self.col:
            raise error("fail: col of 1st matrix != row of 2nd matrix")

        result = Matrix(self.row, matrixB.col)
        for i in range(self.row):
            for j in range(matrixB.col):
                for k in range(self.col):
                    result[i][j] = result[i][j] + self.arr[i][k] * matrixB[k][j]
        return result

    def __str__(self):
        stri = ""
        for i in xrange(len(self.arr)):
            if i is not 0:
                stri += "\n"
            for j in xrange(len(self.arr[i])):
		num  = self.arr[i][j]
		if num < 10000000:
                	stri += str(self.arr[i][j]) + " "
		else:
			stri += "%.3e" % num + " "
	stri += "\n"
        return stri




				
