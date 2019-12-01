import ford_fulkerson
from commons import dimacs
import sys

file_name = '../datasets/connectivity/cycle'

V, edges = ford_fulkerson.prepare_graph(file_name, dimacs.loadWeightedGraph)
ans = sys.maxsize

for v1 in range(1, V + 1):
    for v2 in range(1, V + 1):
        if v1 == v2:
            continue
        flow = ford_fulkerson.ford_fulkerson(V, edges, v1, v2)
        if flow > 0:
            ans = min(ans, flow)

print(ans)