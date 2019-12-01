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
