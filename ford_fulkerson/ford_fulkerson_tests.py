import unittest
from ford_fulkerson import ford_fulkerson

graph = "datasets/flow/rand100_500"


class FordFulkersonTest(unittest.TestCase):

    def test_graph_loading(self):
        (V, edges) = ford_fulkerson.prepare_graph(graph)
        self.assertEqual(V, 100)

    def test_find_path_bfs(self):
        (V, edges) = ford_fulkerson.prepare_graph(graph)
        parents = ford_fulkerson.find_path_bfs(V, edges, 1)
        iter = parents[V]
        while parents[iter[0]] != ():
            iter = parents[iter[0]]

        self.assertEqual(1, iter[0])

    def test_find_min_in_path(self):
        parents = [(), (0, 4, 1), (1, 10, 2)]
        min_val = ford_fulkerson.find_min_in_path(parents, 2)
        self.assertEqual(4, min_val)