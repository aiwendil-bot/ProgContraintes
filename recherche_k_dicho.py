from parser import parser
from Modele_2 import satisfiabilite_model2


def recherche_dicho(filename):
    graph = parser(filename)
    degrees = [len(k) for k in graph.values()]
    inf = int(max(degrees) / 2)
    print(inf)
    sup = int(len(graph) / 2)
    k = int(len(graph) / 4)

    while sup - inf > 2:
        print(inf,sup)
        if satisfiabilite_model2(filename, k):
            sup = k
        else:
            inf = k
        k = int((sup - inf) / 2) + inf
    if satisfiabilite_model2(filename, k):
        return k
    else:
        return sup


print(recherche_dicho("Instances/ibm32.mtx.rnd"))