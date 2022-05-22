from gurobipy import tuplelist, Model, GRB
import matplotlib.pyplot as plt
import networkx as nx


def SPP(links, cost, origin, destination):
    m = Model('SPP')
    x = m.addVars(links, obj=cost, name="flow")
    for i in range(1, len(links) - 3):
        m.addConstr(sum(x[i, j] for i, j in links.select(i, '*')) - sum(x[j, i] for j, i in links.select('*', i)) ==
        (1 if i == origin else -1 if i == destination else 0), 'node%s_' % i)
    m.optimize()
    if m.status == GRB.Status.OPTIMAL:
        print('The final solution is:')
        for i, j in links:
            if(x[i, j].x > 0):
                print(i, j, x[i, j].x)
    G = nx.DiGraph()
    list_nodes = list(range(1, len(links) - 3))
    G.add_nodes_from(list_nodes)
    for i, j in links:
        G.add_edge(i, j)
    node_pos = {1: (0, 0), 2: (2, 2), 3: (2, -2), 4: (5, 2), 5: (5, -2), 6: (7, 0)}
    red_edges = [(i, j) for i, j in links if x[i, j].x > 0]
    sp = [i for i, j in links if x[i, j].x > 0]
    sp.append(destination)
    node_col = ['white' if not node in sp else 'red' for node in G.nodes()]
    edge_col = ['black' if not edge in red_edges else 'red' for edge in G.edges()]
    nx.draw_networkx(G, node_pos, node_color=node_col, node_size=450)
    nx.draw_networkx_edges(G, node_pos, edge_color=edge_col)
    nx.draw_networkx_edge_labels(G, node_pos, edge_labels=cost)
    plt.axis('off')
    plt.show()


links = tuplelist([(1, 2), (1, 3), (2, 3), (2, 4), (2, 5), (3, 5), (4, 6), (5, 4), (5, 6)])
cost = {(1, 2): 2, (1, 3): 4, (2, 3): 1, (2, 4): 4, (2, 5): 2, (3, 5): 3, (4, 6): 2, (5, 4): 3, (5, 6): 2}
SPP(links, cost, 1, 6)


def LPP(links, cost, origin, destination):
    m = Model('LPP')
    x = m.addVars(links, obj=cost, name="flow")
    for i in range(1, len(links) - 3):
        m.addConstr(sum(x[i, j] for i, j in links.select(i, '*')) - sum(x[j, i] for j, i in links.select('*', i)) ==
        (1 if i == origin else -1 if i == destination else 0), 'node%s_' % i)
        
    m.optimize()
    if m.status == GRB.Status.OPTIMAL:
        print('The final solution is:')
        for i, j in links:
            if(x[i, j].x > 0):
                print(i, j, x[i, j].x)
    
    
    G = nx.DiGraph()
    list_nodes = list(range(1, len(links) - 3))
    G.add_nodes_from(list_nodes)
    for i, j in links:
        G.add_edge(i, j)
    node_pos = {1: (0, 0), 2: (2, 2), 3: (2, -2), 4: (5, 2), 5: (5, -2), 6: (7, 0)}
    red_edges = [(i, j) for i, j in links if x[i, j].x > 0]
    sp = [i for i, j in links if x[i, j].x > 0]
    sp.append(destination)
    node_col = ['white' if not node in sp else 'red' for node in G.nodes()]
    edge_col = ['black' if not edge in red_edges else 'red' for edge in G.edges()]
    nx.draw_networkx(G, node_pos, node_color=node_col, node_size=450)
    nx.draw_networkx_edges(G, node_pos, edge_color=edge_col)
    nx.draw_networkx_edge_labels(G, node_pos, edge_labels=cost)
    plt.axis('off')
    plt.show()