from pycsp3 import *

n = data # number of queens, it’s a data
# q[i] is the column where is put the ith queen (at row i)
q = VarArray(size=n, dom=range(n))
satisfy(
AllDifferent(q), # no 2 queens on the same column
# no two queens on the same upward diagonal
AllDifferent(q[i] + i for i in range(n)),
# no two queens on the same downward diagonal
AllDifferent(q[i] - i for i in range(n)))

