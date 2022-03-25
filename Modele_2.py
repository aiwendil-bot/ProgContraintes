from pycsp3 import *
import parser

[file,k] = data
graph = parser.parser(data[0])

n = len(graph)

f = VarArray(size=n, dom=range(1, n+1))
possible = []
for u in range(1,n+1):
    for v in range(1,n+1):
        if (u != v) and min(abs(v - u), n - abs(v - u)) <= k:
            possible.append((u, v))
print("possible : ", possible)
satisfy(
    AllDifferent(f),
    [(f[u-1],f[v-1]) in possible for u in graph.keys() for v in graph[u]]
)

#python Modele_2.py -data=[Instances/didactic.mtx.rnd,10] -solve
#python Modele_2.py -data=[Instances/ibm32.mtx.rnd,10] -solve