import unittest
import stoer_wagner


class StoerWagnerTests(unittest.TestCase):

    def test_vertex_merging(self):
        graph = stoer_wagner.Graph(3)
        graph.add_edge(1, 2, 10)
        graph.add_edge(2, 3, 5)
        graph.add_edge(3, 1, 15)
        graph.merge_vertices(1, 2)

        self.assertEqual(1, len(graph.nodes[1].edges))
        self.assertEqual(20, graph.nodes[1].edges[3])
        self.assertFalse(graph.nodes[2].is_active)
        self.assertEqual(0, len(graph.nodes[2].edges))
        self.assertFalse(2 in graph.nodes[3].edges)

    def test_minimum_cut_phase(self):
        G = stoer_wagner.load_graph("../datasets/stoer_wagner/simple")
        s = stoer_wagner.minimum_cut_phase(G)
        print(s)

    def test_minimum_cut(self):
        G = stoer_wagner.load_graph("../datasets/stoer_wagner/clique200")
        minimum_cut = stoer_wagner.minimum_cut(G)
        print(minimum_cut)
