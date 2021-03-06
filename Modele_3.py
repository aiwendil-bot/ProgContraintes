from pysat.solvers import Glucose4
from parser import parser
import numpy as np
from threading import Timer


def satisfiabilite_model3(filename,k,time):
    cyclic_bandwith = k

    graph = parser(filename)
    n = len(graph)



    A = np.zeros((n+1, n+1), int)
    g = Glucose4()

    for i in range(n+1):
        for j in range(n+1):
            A[i][j] = i * n + j + 1


    A[0][0]=1
    g.add_clause([n**2 + 1])



    def possible(i, j):
        return n ** 2 + 1 if min(abs(j - i), n - abs(j - i)) <= cyclic_bandwith else - (n ** 2 + 1)


    # contrainte 1
    # Minimum un vrai dans chaque ligne

    contrainte1 = []
    for i in range(n):
        contrainte1.append([int(A[i][j]) for j in range(n)])

    g.append_formula(contrainte1)

    # contrainte 2
    # Maximum un vrai dans chaque ligne
    #contrainte2 = []

    #for i in range(n):
     #   for j in range(n):
      #      for l in range(n):
       #         if l != j:
        #            contrainte2.append([-int(A[i][j]), -int(A[i][l])])
    #g.append_formula(contrainte2)

    # contrainte 3
    # Maximum un vrai dans chaque colonne
    contrainte3 = []

    for j in range(n):
        for i in range(n):
            for k in range(n):
                if k != i:
                    contrainte3.append([-int(A[i][j]), -int(A[k][j])])

    g.append_formula(contrainte3)
    # contrainte 4
    # Vérification de l'étiquetage possible pour chaque arête
    contrainte4 = []

    for i in graph.keys():
        for k in graph[i]:
            for j in range(1, n + 1):
                for l in range(1, n + 1):
                    if l != j:
                        contrainte4.append([-int(A[i - 1][j - 1]), -int(A[k - 1][l - 1]), possible(j, l)])
    g.append_formula(contrainte4)

    timer = Timer(time, interrupt, [g])
    timer.start()
    print(g.solve_limited(expect_interrupt=True))
    print(g.get_model())


    def solution_to_etiquetage(solution, n):
        res = []
        for i in range(n ** 2):
            if solution[i] > 0:
                res.append((i // n + 1, i % n + 1))
        return res

    g.clear_interrupt()
    #print(solution_to_etiquetage(g.get_model(), 32))


def interrupt(s):
    s.interrupt()
    s.clear_interrupt()

#print(satisfiabilite_model3("Instances/pores_1.mtx.rnd",8,10))
