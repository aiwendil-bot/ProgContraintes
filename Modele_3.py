from pysat.solvers import Solver, Glucose3
import parser
import numpy as np

k = 9

graph = parser.parser('Instances/ibm32.mtx.rnd')
n = len(graph)
#boolMatrix = np.zeros(2,2)

A = np.zeros((n,n),int)
g = Glucose3()
#    g.add_clause([i*n+j for j in range(1,n+1)])
# print(graph)

for i in range(0,n):
    for j in range(0, n):
        A[i][j] = i*n + j + 1

print(A)

g.add_clause([n**2 + 1])

def possible(i,j,k,n):
    if (min(abs(j-i),n-abs(j-i)) <= k & i != j):
        return (n**2 + 1)
    else:
        return (- (n**2 + 1))

#contrainte 1
# Minimum un vrai dans chaque lignes
for i in range(0,n):
    g.add_clause([int(A[i][j]) for j in range(0, n)])

# #contrainte 2
# Maximum un vrai dans chaque lignes
# for i in range(0,n):
#     for j in range(0, n):
#         for l in range(0, n):
#             if l != j:
#                 g.add_clause([-int(A[i][j]),-int(A[i][l])])

#contrainte 3
# Maximum un vrai dans chaque colonne
for j in range(0,n):
    for i in range(0, n):
        for k in range(0, n):
            if k != i:
                g.add_clause([-int(A[i][j]), -int(A[k][j])])


#contrainte 4
# Vérification de l'étiquetage possible pour chaque arêtes
for i in graph.keys():
    for kk in graph[i]:
        for j in range(1,n+1):
            for l in range(1,n+1):
                if l != j:
                    g.add_clause([-int(A[i-1][j-1]),-int(A[kk-1][l-1]),possible(j,l,k,n)])

print(g.solve())
print(g.get_core())
print(g.get_model())