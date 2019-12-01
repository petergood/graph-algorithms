from commons import dimacs


class Node:
    def __init__(self, id):
        self.id = id
        self.edges = {}
        self.is_active = True

    def add_edge(self, to, weight):
        if to != self.id:
            self.edges[to] = self.edges.get(to, 0) + weight

    def remove_edge(self, to):
        del self.edges[to]


class Graph:
    def __init__(self, vertex_count):
        self.v = vertex_count
        self.nodes = [Node(i) for i in range(vertex_count + 1)]

    def merge_vertices(self, x, y):
        to_delete = []
        for node in self.nodes[y].edges:
            del self.nodes[node].edges[y]
            w = self.nodes[y].edges[node]
            self.nodes[x].add_edge(node, w)
            self.nodes[node].add_edge(x, w)
            to_delete.append(node)
        for node in to_delete:
            del self.nodes[y].edges[node]
        self.nodes[y].is_active = False

    def add_edge(self, x, y, w):
        self.nodes[x].add_edge(y, w)
        self.nodes[y].add_edge(x, w)