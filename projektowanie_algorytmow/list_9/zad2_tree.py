from collections import defaultdict
import networkx as nx
from matplotlib import pyplot as plt


class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v):
                    return True
            elif i != parent:
                return True
        return False

    def is_tree(self):
        visited = [False] * self.V
        if self.is_cyclic_util(0, visited, -1):
            return False
        for i in range(self.V):
            if not visited[i]:
                return False
        return True


def visualize(e):
    g = nx.Graph()
    g.add_edges_from(e)
    g_pos = nx.spring_layout(g)
    nx.draw_networkx(g, pos=g_pos, node_size=800)
    plt.show()


if __name__ == "__main__":
    g1 = Graph(5)
    g1.add_edge(1, 0)
    g1.add_edge(0, 2)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)
    e1 = [(1, 0), (0, 2), (0, 3), (3, 4)]
    visualize(e1)

    g2 = Graph(5)
    g2.add_edge(1, 0)
    g2.add_edge(0, 2)
    g2.add_edge(2, 1)
    g2.add_edge(0, 3)
    g2.add_edge(3, 4)
    e2 = [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)]