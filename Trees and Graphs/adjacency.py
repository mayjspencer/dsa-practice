class GraphMatrix:
    def __init__(self, num_nodes):
        self.matrix = [[False] * num_nodes for _ in range(num_nodes)]

    def add_edge(self, u, v):
        self.matrix[u][v] = True

    def has_edge(self, u, v):
        return self.matrix[u][v]


class GraphList:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def get_neighbors(self, u):
        return self.graph.get(u, [])


def test_graph_representation():
    print("Testing Matrix...")
    g_matrix = GraphMatrix(5)
    g_matrix.add_edge(0, 1)
    g_matrix.add_edge(1, 2)
    assert g_matrix.has_edge(0, 1) == True
    assert g_matrix.has_edge(1, 0) == False

    print("Testing List...")
    g_list = GraphList()
    g_list.add_edge('A', 'B')
    g_list.add_edge('A', 'C')
    assert set(g_list.get_neighbors('A')) == {'B', 'C'}
    assert g_list.get_neighbors('B') == ['A']
    assert g_list.get_neighbors('C') == ['A']

    print("All tests passed.")

test_graph_representation()
