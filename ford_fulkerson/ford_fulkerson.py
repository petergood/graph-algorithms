from commons import dimacs
import collections
import sys

# todo: use better data structure for representing graph

def prepare_graph(file_name):
    (V, L) = dimacs.loadDirectedWeightedGraph(file_name)
    edges = []
    for i in range(V + 1):
        edges.append([])
        for j in range(V + 1):
            edges[i].append(0)
    for e in L:
        edges[e[0]][e[1]] = e[2]

    return V, edges


def find_path_bfs(V, edges, start_node, end_node):
    parents = []
    visited = []
    for _ in range(V + 1):
        parents.append(())
        visited.append(False)

    queue = collections.deque()
    queue.append(start_node)
    visited[start_node] = True

    while len(queue) > 0:
        node = queue.popleft()
        for neigh in range(V + 1):
            w = edges[node][neigh]
            if edges[node][neigh] > 0 and not visited[neigh]:
                queue.append(neigh)
                visited[neigh] = True
                parents[neigh] = (node, w, neigh) #parent, weight, current node

    return parents


def find_min_in_path(parents, end_node):
    iter = parents[end_node]
    min_val = sys.maxsize
    while parents[iter[0]] != ():
        min_val = min(min_val, iter[1])
        iter = parents[iter[0]]
    return min(min_val, iter[1])


def ford_fulkerson(V, edges, start_node, end_node):
    max_flow = 0
    while True:
        parents = find_path_bfs(V, edges, start_node, end_node)
        if parents[end_node] == ():
            break

        min_val = find_min_in_path(parents, V)
        max_flow += min_val
        it = parents[end_node]
        while parents[it[0]] != ():
            edges[it[0]][it[2]] -= min_val
            edges[it[2]][it[0]] += min_val
            it = parents[it[0]]

        edges[it[0]][it[2]] -= min_val
        edges[it[2]][it[0]] += min_val

    return max_flow


