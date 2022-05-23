import networkx as nx
import matplotlib.pyplot as plt
import random


#1.4
def circular_graph(n):
    plt.figure(1, figsize=(12, 12))
    g = nx.Graph()
    vv = list(range(1, n+1, 1))
    for v1 in vv:
        for v2 in vv:
            g.add_edge(v1, v2, weight=1)
    g.add_edge(vv[0], vv[len(vv)-1])
    pos = nx.circular_layout(g)
    nx.draw_networkx_nodes(g, pos, node_size=200)
    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_edges(g, pos)
    plt.show()


#1.5
def random_graph(n):
    plt.figure(2, figsize=(5, 5))
    g = nx.Graph()
    vv = list(range(1, n+1, 1))
    vx = {}
    vy = {}
    pos = {}
    newvv = []
    index = 1
    for v in vv:
        index = 1
        while index <= 100:
            vx[v] = random.randint(1, 20)
            vy[v] = random.randint(1, 20)
            if [vx[v], vy[v]] not in pos.items():
                pos[v] = [vx[v], vy[v]]
                g.add_node(v)
                newvv.append(v)
                break
            else:
                index += 1
                if index == 100:
                    msg = "Nie udalo sie dokonczyc tworzenia grafu"
                    plt.show()
                    print(msg)
                    return 0
    nx.draw_networkx_nodes(g, pos, node_size=1000)
    for v1 in newvv:
        for v2 in newvv:
            g.add_edge(v1, v2, weight=1)
    nx.draw_networkx_edges(g, pos)
    plt.show()


circular_graph(10)
#andom_graph(10)


'''w zadaniu 5 nie zostaly narzucone rozmiary okna oraz wielkosc wierzcholka
zatem zaimplementowałem to zgodnie z poleceniem natomiast teorytycznie
wystarczyloby zmienic wielkosc node_size i juz zadanie zmieniloby swoje zalozenia'''
