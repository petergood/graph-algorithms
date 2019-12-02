from commons import dimacs
from queue import PriorityQueue
import sys


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

    def find_random_neighbour(self):
        return list(self.edges)[0]

    def __lt__(self, other):
        return self.id < other.id


class Graph:
    def __init__(self, vertex_count):
        self.v = vertex_count
        self.active_nodes = vertex_count
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
        self.active_nodes = self.active_nodes - 1

    def find_lowest_active_node(self):
        for node in self.nodes:
            if node.id != 0 and node.is_active:
                return node
        return None

    def add_edge(self, x, y, w):
        self.nodes[x].add_edge(y, w)
        self.nodes[y].add_edge(x, w)


def minimum_cut_phase(graph):
    start_node = graph.find_lowest_active_node()
    s = {start_node.id: True}
    vertex_order = [start_node.id]
    weights = [0 for _ in range(graph.v + 1)]
    queue = PriorityQueue()
    queue.put((0, graph.nodes[start_node.find_random_neighbour()]))

    while not queue.empty():
        node = queue.get()[1]
        if node.id in s:
            continue
        s[node.id] = True
        vertex_order.append(node.id)

        for n in node.edges:
            weights[n] = weights[n] + node.edges[n]
            queue.put((-weights[n], graph.nodes[n]))

    s = vertex_order[len(vertex_order) - 1]
    t = vertex_order[len(vertex_order) - 2]
    sum_from_s = 0
    for n in graph.nodes[s].edges:
        sum_from_s = sum_from_s + graph.nodes[s].edges[n]

    graph.merge_vertices(s, t)

    return sum_from_s


def minimum_cut(graph):
    min_cut = sys.maxsize
    while graph.active_nodes > 1:
        pot = minimum_cut_phase(graph)
        min_cut = min(min_cut, pot)

    return min_cut


def load_graph(file_path):
    V, L = dimacs.loadDirectedWeightedGraph(file_path)
    G = Graph(V)

    for edge in L:
        G.add_edge(edge[0], edge[1], edge[2])

    return G
