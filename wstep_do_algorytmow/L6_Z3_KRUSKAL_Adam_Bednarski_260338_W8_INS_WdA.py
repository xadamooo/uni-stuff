#  %%
import networkx as nx
from matplotlib import pyplot as plt


def make_set(vertice):
    parent[vertice] = vertice


def find_parent(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find_parent(parent[vertice])
    return parent[vertice]


def link(u, v, edges):
    ancestor1 = find_parent(u)
    ancestor2 = find_parent(v)
    if ancestor1 != ancestor2:
        for edge in edges:
            parent[ancestor1] = ancestor2


def kruskal(graph):
    mst = set()
    for vertice in graph['V']:
        make_set(vertice)

    edges = list(graph['E'])
    edges.sort()
    for edge in edges:
        weight, u, v = edge
        if find_parent(u) != find_parent(v):
            mst.add(edge)
            link(u, v, edges)
    return mst


def visualize(verts, edges):
    G = nx.Graph()
    for vert in verts:
        G.add_nodes_from(verts)
    for edge in edges:
        G.add_edge(edge[1], edge[2], weight=edge[0])
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


graph = {
        'V': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        'E': set([
            (2, '1', '2'),
            (2, '1', '3'),
            (2, '2', '3'),
            (1, '2', '6'),
            (1, '3', '4'),
            (5, '4', '6'),
            (4, '6', '7'),
            (7, '4', '5'),
            (6, '7', '5'),
            (1, '4', '10'),
            (2, '5', '10'),
            (8, '5', '8'),
            (2, '5', '9'),
            (3, '8', '9'),
            ])
        }
parent = dict()
mst = kruskal(graph)
print(f'Minimal Spanning Tree using Kruskal Algorithm:{mst}')
mst_weight = 0
for edge in mst:
    weight, u, v = edge
    mst_weight += weight

print("Cost: ")
print(mst_weight)
visualize(graph['V'], mst)

# %%
