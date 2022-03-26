from pysat.solvers import Glucose4
import parser
import numpy as np

cyclic_bandwith = 15

graph = parser.parser('Instances/ibm32.mtx.rnd')
n = len(graph)

A = np.zeros((n, n), int)
g = Glucose4()

for i in range(n):
    for j in range(n):
        A[i][j] = i * n + j + 1

g.add_clause([n ** 2 + 1])


def possible(i, j):
    return n ** 2 + 1 if min(abs(j - i), n - abs(j - i)) <= cyclic_bandwith & i != j else - (n ** 2 + 1)


# contrainte 1
# Minimum un vrai dans chaque ligne
for i in range(n):
    g.add_clause([int(A[i][j]) for j in range(n)])
# contrainte 2
# Maximum un vrai dans chaque ligne
for i in range(n):
    for j in range(n):
        for l in range(n):
            if l != j:
                g.add_clause([-int(A[i][j]), -int(A[i][l])])

# contrainte 3
# Maximum un vrai dans chaque colonne
for j in range(n):
    for i in range(n):
        for k in range(n):
            if k != i:
                g.add_clause([-int(A[i][j]), -int(A[k][j])])

# contrainte 4
# Vérification de l'étiquetage possible pour chaque arête
for i in graph.keys():
    for k in graph[i]:
        for j in range(1, n + 1):
            for l in range(1, n + 1):
                if l != j:
                    g.add_clause([-int(A[i - 1][j - 1]), -int(A[k - 1][l - 1]), possible(j, l)])

print(g.solve())
print(g.get_model())


def solution_to_etiquetage(solution, n):
    res = []
    for i in range(n ** 2):
        if solution[i] > 0:
            res.append((i // n + 1, i % n + 1))
    return res


#print(solution_to_etiquetage(g.get_model(), 32))
