#  %%
import networkx as nx
from matplotlib import pyplot as plt


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]for row in range(vertices)]

    def visualizeMST(self, tree):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(tree[i], "-", i, "\t", self.graph[i][tree[i]])

    def minkey(self, key, mstSet):
        min = float('inf')
        for v in range(self.V):
            if key[v] < min and mstSet[v] is False:
                min = key[v]
                min_index = v
        return min_index

    def prim(self):
        key = [float('inf')] * self.V
        tree = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        tree[0] = -1
        for cout in range(self.V):
            u = self.minkey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] is False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    tree[v] = u
        self.visualizeMST(tree)
        self.visualizenx(tree)

    def visualizenx(self, tree):
        G = nx.Graph()
        for i in range(1, self.V):
            G.add_node(tree[i])
        for i in range(1, self.V):
            G.add_edge(tree[i], i, weight=self.graph[i][tree[i]])
        pos = nx.spectral_layout(G)
        options = {
            "font_size": 10,
            "node_size": 500,
            "node_color": "pink",
            "edgecolors": "black",
            "linewidths": 3,
            "width": 2,
        }
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw_networkx(G, pos, **options)
        ax = plt.gca()
        ax.margins(0.2)
        plt.show()


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]
g.prim()
# %%
