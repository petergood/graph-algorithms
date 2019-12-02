from commons import dimacs


class Node:
    def __init__(self, id):
        self.id = id
        self.neighbours = []


class Graph:
    def __init__(self, v, edges):
        self.v = v
        self.nodes = []
        for i in range(v):
            self.nodes.append(Node(i))

        self._load_graph(edges)

    def _load_graph(self, edges):
        for edge in edges:
            self.nodes[edge[0] - 1].neighbours.append(self.nodes[edge[1] - 1])
            self.nodes[edge[1] - 1].neighbours.append(self.nodes[edge[0] - 1])


def lex_dfs(graph):
    ordering = []
    sets = [set([i for i in range(graph.v)])]

    while len(sets) > 0:
        elem = sets[len(sets) - 1].pop()
        if len(sets[len(sets) - 1]) == 0:
            sets.pop()
        ordering.append(elem)
        new_sets = []
        for i in range(len(sets)):
            neighbours = []
            for neighbour in graph.nodes[elem].neighbours:
                if neighbour.id in sets[i]:
                    neighbours.append(neighbour.id)
            y = set(neighbours)
            k = sets[i] - y

            if len(y) > 0:
                new_sets.append(y)
            if len(k) > 0:
                new_sets.append(k)

        sets = new_sets

    return ordering
