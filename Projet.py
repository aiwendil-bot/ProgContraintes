from pycsp3 import *
import parser

file = data
graph = parser.parser(data)

print(graph)

n = len(graph)
#x = Var ({range (n)})
#i = len(DictS[x])
#j = len(DictS[x])
f = VarArray(size=n, dom=range(1,n+1))
#print("    ")
#print(f)

satisfy(
    # Contrainte de
    AllDifferent(f)
)

minimize(
    Maximum(Minimum(abs(f[i-1]-f[j-1]), n - abs(f[i-1] - f[j-1])) for i in graph.keys() for j in graph[i])
)