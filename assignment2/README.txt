
COMSW3251 hw2
jcf2167
Jessica Fan 

TO RUN: $python main.py input.txt output.txt

1.) the elimination is done in function called eliminateOptimized which 
uses the fact that for each column of the matrix, you need only eliminate up to the width of the diagonal, m, rather than n, since multiplying 0 by a number just give syou 0 anyways. Thus for each row, the for loop is changed to only compute for the width of the diagonal, unless the function is near the bottom of the matrix, which then we just compute to n. 

Then, solve(mat, b, m)  solves Ax=b using L and U from eliminateOptimized(A,m) and also only takes the size of diagonal into consideration

Elimination is reduced to O(mn^2). 

3.)
$python main.py input.txt output.txt 

note: for input
n is the first line
m is the second line
b is the third line
matrix starts in the fourth line

for output:
the output is just the solution x 
