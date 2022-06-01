#  %%
import random
import networkx as nx
from matplotlib import pyplot as plt
from queue import Queue


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        return data

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


def generateGraph(size, maxValue):
    graph = Graph()
    while len(graph.getVertices()) < size:
        v1 = random.randint(1, maxValue)
        v2 = random.randint(1, maxValue)
        if v1 == v2:
            continue
        else:
            graph.addEdge(v1, v2)
            graph.addEdge(v2, v1)
    return graph


def connectedComponents(graph):
    c = [0 for x in range(len(graph.getVertices()))]
    count = 0
    S = Stack()
    for vertex in graph:
        if c[vertex.getId() - 1] > 0:   
            continue
        count += 1
        S.push(vertex)
        c[vertex.getId() - 1] = count
        while not S.is_empty():
            v = S.pop()
            for neighbour in v.getConnections():
                if c[neighbour.getId() - 1] > 0:
                    continue
                S.push(neighbour)
                c[neighbour.getId() - 1] = count

    for i in range(1, count + 1):
        print(f"Składowa nr {i}: \nWierzchołki:")
        for j in graph:
            if c[j.getId() - 1] == i:
                print(j.getId())


def visualize(graph):
    G = nx.Graph()
    for vertex in graph:
        for connection in vertex.getConnections():
            G.add_edge(vertex.getId(), connection.getId())
    pos = nx.random_layout(G)
    options = {
        "font_size": 18,
        "node_size": 1500,
        "node_color": "pink",
        "edgecolors": "black",
        "linewidths": 3,
        "width": 2,
    }
    nx.draw_networkx(G, pos, **options)
    ax = plt.gca()
    ax.margins(0.1)
    plt.show()


graph = generateGraph(7, 7)
connectedComponents(graph)
visualize(graph)
#  %%


class DijkstraAlgorithm:
    def __init__(self, nxGraph):
        self.graph = nxGraph

    def Path(self, start, stop):
        Q = Queue()
        distances = {v: float('inf') for v in sorted(list(self.graph.nodes))}
        visited = set()
        distances[start] = 0
        Q.put(start)
        while Q.empty() is not True:
            u = Q.get()
            visited.add(u)
            for neighbour in dict(self.graph.adjacency()).get(u):
                data = self.graph.get_edge_data(u, neighbour)
                alt = distances[u] + data['weight']
                if alt < distances[neighbour]:
                    distances[neighbour] = alt
                if neighbour not in visited:
                    visited.add(neighbour)
                    Q.put(neighbour)
        print(f"Distances: {distances}")
        print(f"Najkrótsza odległość od {start} do {stop} to {distances[stop]}")


G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_edge(1, 5, weight = 1)
G.add_edge(1, 2, weight = 3)
G.add_edge(4, 3, weight = 7)
G.add_edge(3, 2, weight = 2)
dijkstra = DijkstraAlgorithm(G)
dijkstra.Path(1, 5)
pos = nx.random_layout(G)
options = {
    "font_size": 18,
    "node_size": 1500,
    "node_color": "pink",
    "edgecolors": "black",
    "linewidths": 3,
    "width": 2,
}
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
nx.draw_networkx(G, pos, **options)
ax = plt.gca()
ax.margins(0.1)
plt.show()

# %%
# %%
