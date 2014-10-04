Jcf2167
September 23, 2014
Programming Assignment #1

TO COMPILE: 
python prog1.py input.txt output.txt

I created a Matrix object which lets you create a matrix of NxM dimensions from an 2-dimensional string array where each entry represents a row from a matrix. The Matrix object lets you access its entries with syntax: matrix[][] and do Matrix multiplication/addition with another Matrix object (it returns a new Matrix object with the results). 

The program takes a matrix and then computes A^(2^k) using k multiplications recursively. It computes (using the redefined * operator in the Matrix class) A*A = A^2 and then A^2  * A^2 = A^4 and then A^4 * A^4= A^8 until it reaches A^(2^k).  For each recursive call, 2^k is divided by 2 until the base case 2^k/2=1 which is just A^1.

Allows decimals and whole numbers. If number is larger than 10,000,000, it is displayed in scientific notation. 



