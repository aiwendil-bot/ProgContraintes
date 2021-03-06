from parser import parser
from Modele_2 import satisfiabilite_model2
from math import *


def recherche_dicho(filename,time):
    graph = parser(filename)
    degrees = [len(k) for k in graph.values()]
    inf = ceil(max(degrees) / 2)
    sup = floor(len(graph) / 2)
    k = floor((sup + inf)/2)

    while sup - inf > 2:
        if satisfiabilite_model2(filename, k,time):
            sup = k
        else:
            inf = k
        k = floor((sup - inf) / 2) + inf
    if satisfiabilite_model2(filename, k, time):
        return k
    else:
        return sup


#print(recherche_dicho("Instances/ibm32.mtx.rnd"))
