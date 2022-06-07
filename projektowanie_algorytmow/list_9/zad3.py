from collections import defaultdict
import networkx as nx
from matplotlib import pyplot as plt

class Graph:
    def __init__(self,n):
        self.graph = defaultdict(list)
        self.N = n

    def addEdge(self,m,n,w):
        visited = [False] * self.N
        self.graph[m].append(n)
        if self.is_cyclic_util(n, visited, -1):
            print('Blad grafu')

    def sortUtil(self,n,visited,stack):
        visited[n] = True
        for element in self.graph[n]:
            if visited[element] == False:
                self.sortUtil(element,visited,stack)
        stack.insert(0,n)

    def topologicalSort(self):
        visited = [False]*self.N
        stack = []
        for element in range(self.N):
            if visited[element] == False:
                self.sortUtil(element, visited, stack)
        return stack

    def is_cyclic_util(self, n, visited, parent):
        visited[n] = True
        for i in self.graph[n]:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, n):
                    return True
            elif i != parent:
                return True
        return False


def visualize(edges, weights, state):
    g = nx.DiGraph()
    g.add_edges_from(edges)
    if state == 'ns':
        for i, e in enumerate(edges):
            a, b = e
            g[a][b]['weight'] = weights[i]
    elif state == 's':
        for i in edges:
            if i not in weights:
                weights[i] = 0
        for i in weights:
            a, b = i
            g[a][b]['weight'] = weights[(a, b)]

    g_pos = nx.spring_layout(g)
    nx.draw_networkx(g, pos=g_pos, node_size=800)
    edge_labels = dict([((u, v), d['weight']) for u,v,d in g.edges(data=True) if d['weight'] > 0])
    nx.draw_networkx_edge_labels(g, pos=g_pos, edge_labels=edge_labels)
    plt.show()

if __name__ == "__main__":
    graph = Graph(5)
    graph.addEdge(0,1,2)
    graph.addEdge(0,3,1)
    graph.addEdge(1,2,4)
    graph.addEdge(2,3,3)
    graph.addEdge(2,4,2)
    graph.addEdge(3,4,5)

    edges = [(0,1), (0,3), (1,2), (2,3), (2,4), (3,4)]
    weights = [2, 1, 4, 3, 2, 5]
    res = 0
    times = {}
    visualize(edges, weights, 'ns')
    print("Kolejnosc wykonania działań:")
    order = graph.topologicalSort()
    print(order)
    for i in range(len(order)-1, 0, -1):
        res += weights[edges.index((i-1, i))]
        times[(order[i-1], order[i])] = res
    print(f'Czas wykonania działań: {res}')
    visualize(edges, times, 's')
