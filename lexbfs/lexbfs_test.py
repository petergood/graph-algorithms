import unittest
from commons import dimacs
import lexbfs


class LexBFSTest(unittest.TestCase):
    def test_lexbfs(self):
        v, l = dimacs.loadWeightedGraph("../datasets/chordal/interval-rnd6")
        g = lexbfs.Graph(v, l)
        print(lexbfs.lex_dfs(g))
