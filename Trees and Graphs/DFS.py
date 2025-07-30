# DFS Practice
class DFSGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_recursive(self, start, visited = None):
        if visited == None:
            visited = set()

        if start in visited:
            return
        
        print(start)
        visited.add(start)

        for neighbor in self.graph.get(start,[]):
            self.dfs_recursive(neighbor, visited)

    def dfs_iterative(self, start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()

            if node in visited:
                continue
            print(node)
            visited.add(node)

            for neighbor in reversed(self.graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)


def test_dfs():
    g = DFSGraph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('E', 'F')

    print("Recursive DFS:")
    g.dfs_recursive('A')

    print("\nIterative DFS:")
    g.dfs_iterative('A')

test_dfs()
