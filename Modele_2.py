from pycsp3 import *
import parser

[file,k] = data
graph = parser.parser(data[0])

n = len(graph)

f = VarArray(size=n, dom=range(1, n+1))
liste_couples = [(i,j) for i in range(1,n+1) for j in range(1,n+1)]
possible = []
for u in graph.keys():
    for v in graph[u]:
        if (u != v) and min(abs(v - u), n - abs(v - u)) <= k:
            possible.append((u, v))
print(possible)
satisfy(
    AllDifferent(f),
    ((f[u-1],f[v-1]) in possible for (u,v) in liste_couples)
)