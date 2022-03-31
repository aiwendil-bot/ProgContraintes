from pycsp3 import *
import parser

#[file,k] = data
#graph = parser.parser(data[0])

#n = len(graph)

#f = VarArray(size=n, dom=range(1, n+1))
#possible = []
#for u in range(1,n+1):
#   for v in range(1,n+1):
#       if (u != v) and min(abs(v - u), n - abs(v - u)) <= k:
#           possible.append((u, v))
#print("possible : ", possible)
#satisfy(
#   AllDifferent(f),
#   [(f[u-1],f[v-1]) in possible for u in graph.keys() for v in graph[u]]
#)

def satisfiabilite_model2(filename,k):
    clear()
    graph = parser.parser(filename)

    n = len(graph)

    f = VarArray(size=n, dom=range(1, n + 1))

    possible = []
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if (u != v) and min(abs(v - u), n - abs(v - u)) <= k:
                possible.append((u, v))

    satisfy(
        f[1] == 1,
        f[2]>f[n-1],
        AllDifferent(f),
        [(f[u - 1], f[v - 1]) in possible for u in graph.keys() for v in graph[u]]
    )

    # instance = compile()
    # ace = solver(ACE)
    # result = ace.solve(instance)
    # print(result)
    #clear()
    # return result is SAT
    file = (filename.split("/")[1]).split(".")[0]
    return (solve(solver=ACE,verbose=2,options="-t=10s,-output="+file+".xml")) is SAT

#print(satisfiabilite_model2("Instances/fs_680_1.mtx.rnd",680))
#print(satisfiabilite_model2("Instances/ibm32.mtx.rnd",8))
print(satisfiabilite_model2("Instances/west0132.mtx.rnd",66))

#python Modele_2.py -data=[Instances/didactic.mtx.rnd,10] -solve
#python Modele_2.py -data=[Instances/ibm32.mtx.rnd,10] -solve



# (solve(solver=ACE,verbose=2,options="-t=1s")) is SAT
