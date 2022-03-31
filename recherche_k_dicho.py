from parser import parser
from Modele_2 import satisfiabilite_model2


def recherche_dicho(filename,time):
    graph = parser(filename)
    degrees = [len(k) for k in graph.values()]
    inf = int(max(degrees) / 2)
    sup = int(len(graph) / 2)
    k = int(len(graph) / 4)

    while sup - inf > 2:
        print(inf,sup)
        if satisfiabilite_model2(filename, k,time):
            sup = k
        else:
            inf = k
        k = int((sup - inf) / 2) + inf
    if satisfiabilite_model2(filename, k, time):
        return k
    else:
        return sup


#print(recherche_dicho("Instances/ibm32.mtx.rnd"))
