import networkx as nx
from matplotlib import pyplot as plt
plt.rcParams['axes.facecolor'] = 'antiquewhite'
plt.rcParams["figure.figsize"] = (7, 6)


def bfs(graph, node):
    global g, g_pos
    visited = [node]
    queue = []
    queue.append(node)
    while queue:
        m = queue.pop(0)
        color_map = ['blue' if curr == m else 'white' for curr in g]
        nx.draw_networkx(g, pos=g_pos, node_color=color_map, node_size=800)
        # plt.show()
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited


def dfs(visited, graph, node):
    global g, g_pos
    if node not in visited:
        color_map = ['blue' if curr == node else 'white' for curr in g]
        nx.draw_networkx(g, pos=g_pos, node_color=color_map, node_size=800)
        plt.show()
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def check_connections(graph):
    if sorted(list(graph.keys())) == sorted(list(bfs(graph, '5'))):
        print('connected components')
    else:
        print('not good')


if __name__ == "__main__":
    graph = {
      '5': ['3', '7'],
      '3': ['2', '4'],
      '7': ['1'],
      '2': [],
      '4': ['8'],
      '8': [],
      '1': []
            }
    visited = []
    g = nx.DiGraph(graph)
    g_pos = nx.spring_layout(g)

