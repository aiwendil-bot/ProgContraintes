from pycsp3 import *
import parser


def satisfiabilite_model1(filename,time):
    clear()

    graph = parser.parser(filename)

    #print(graph)

    n = len(graph)
    #x = Var ({range (n)})
    #i = len(DictS[x])
    #j = len(DictS[x])
    f = VarArray(size=n, dom=range(1,n+1))
    #f[0] = 1
    #print("    ")
    #print(f)

    satisfy(
        # Contrainte de
        AllDifferent(f),
        f[1] == 1,
        f[2]>f[n-1]
    )

    minimize(
        Maximum(Minimum(abs(f[i-1]-f[j-1]), n - abs(f[i-1] - f[j-1])) for i in graph.keys() for j in graph[i])
    )

    return (solve(solver=ACE,verbose=0,options="-t="+time+"s")) is SAT


# bcspwr01
# bcspwr02
# bcsstk01
# curtis54
# ibm32
# pores_1
# will57

# python3  Modele_1.py -data=["Instances/fs_680_1.mtx.rnd"] -solve