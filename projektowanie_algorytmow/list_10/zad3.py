import matplotlib.pyplot as plt
import networkx as nx, numpy as np
from networkx.algorithms import bipartite
from scipy.sparse import csc_matrix

class bpm:
    def __init__(self, graph):
        self.graph = graph

    def max_bipartite_match(self):
        g1 = [-1] * len(self.graph)
        result = 0
        for node_g1 in range(len(self.graph)):
            seen_g2 = [False] * len(self.graph)
            if self.dfs(node_g1, g1, seen_g2):
                result += 1
        return result, g1

    def dfs(self, u, g1, seen_g2):
        for v in range(len(self.graph)):
            if self.graph[u][v] > 0 and seen_g2[v] is False:
                seen_g2[v] = True
                if g1[v] == -1 or self.dfs(g1[v], g1, seen_g2):
                    g1[v] = u
                    return True
        return False


matrix = [[0, 1, 1, 0, 0, 0],
               [1, 0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0],
               [0, 0, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1]]
matrix = np.array(matrix)
g = bpm(matrix)
res, j = g.max_bipartite_match()
G = nx.DiGraph()
U = ['G1'+str(i) for i in range(matrix.shape[0])]
V = ['G2'+str(j) for j in range(matrix.shape[1])]
G.add_nodes_from(U, bipartite=0)
G.add_nodes_from(V, bipartite=1)
G.add_edges_from([(U[i], V[j]) for i, j in zip(*matrix.nonzero())])
for i in G.edges:
    G[i[0]][i[1]]['color'] = 'gray'
for i in range(len(j)):
    G['G1'+str(j[i])]['G2'+str(i)]['color'] = 'blue'
colors = nx.get_edge_attributes(G,'color').values()
RB = nx.complete_bipartite_graph(6, 6)
A = csc_matrix(bipartite.biadjacency_matrix(RB, row_order=bipartite.sets(RB)[0]))
nx.draw_circular(G, edge_color=colors, with_labels=True, node_size=700, width=2, arrowsize=20)
plt.show()


