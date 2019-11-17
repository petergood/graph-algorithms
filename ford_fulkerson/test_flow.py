import ford_fulkerson
import os

path = '../datasets/flow'


def get_ans(file):
    f = open(file, "r")
    lines = f.readlines()
    return int(lines[0].split(' ')[3])


def test_file(file):
    if '_ignore' in file:
        return None

    print("Testing: " + file)
    V, edges = ford_fulkerson.prepare_graph(file)
    ans = get_ans(file)
    flow = ford_fulkerson.ford_fulkerson(V, edges, 1, V)
    print('Expected = ' + str(ans) + ", got = " + str(flow) + ' ' + ('OK' if ans == flow else 'WRONG'))


for r, d, f in os.walk(path):
    for file in f:
        test_file(os.path.join(path, file))