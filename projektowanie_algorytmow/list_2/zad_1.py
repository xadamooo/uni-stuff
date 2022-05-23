import networkx as nx
import matplotlib.pyplot as plt


def get_input(alphabet1):
    text = input("Podaj wejście\n")
    for i in text:
        if i not in alphabet1:
            return -1
    return text


def draw_graph(curr, states, graph_edges):
    color_map = []
    g = nx.Graph()
    for i in states:
        g.add_node(i)
        color_map.append("blue")
    for edge in graph_edges:
        g.add_edge(edge[0], edge[2])
    pos = nx.spring_layout(g)
    color_map[states.index(curr)] = "green"
    nx.draw(g, pos, node_color=color_map, with_labels=True)
    plt.show()


def finite_state_automata(text, graph_edges, states, final_states):
    curr = "q0"
    for char in text:
        for edge in graph_edges:
            if curr == edge[0] and char in edge[1]:
                draw_graph(curr, states, graph_edges)
                curr = edge[2]
                print(f'{edge[0]} --> "{char}" is in {edge[1]} --> {edge[2]}')
                break
    if curr in final_states:
        print("Accept")
    else:
        print("Reject")


states1 = ["q0", "q1", "q2", "q3", "q4", "q5", "q6"]
states2 = ["q0", "q1", "q2", "q3", "q4", "q5"]
graph1_edges = [
    ["q0", ("a", "b", "c"), "q2"],
    ["q2", ("a", "b"), "q1"],
    ["q1", ("c"), "q3"],
    ["q3", ("a", "b", "c"), "q3"],
    ["q1", ("b"), "q0"],
    ["q1", ("a"), "q4"],
    ["q4", ("b", "c"), "q5"],
    ["q5", ("a", "b", "c"), "q4"],
    ["q4", ("a"), "q0"],
    ["q2", ("c"), "q6"],
    ["q6", ("a", "b", "c"), "q3"],
]

graph2_edges = [
    ["q0", ("a"), "q1"],
    ["q1", ("a", "b"), "q2"],
    ["q2", ("b"), "q2"],
    ["q2", ("a", "c"), "q3"],
    ["q3", ("c"), "q3"],
    ["q3", ("b"), "q5"],
    ["q0", ("b", "c"), "q5"],
    ["q1", ("c"), "q5"],
    ["q4", ("a", "b", "c"), "q5"],
    ["q3", ("a"), "q4"],
    ["q5", ("a", "b", "c"), "q5"],
]

final_states = {"graph1": ["q0", "q4", "q5"], "graph2": ["q4"]}
alphabet1 = ["a", "b", "c"]
text = get_input(alphabet1)
if text != -1:
    print(text)
    finite_state_automata(text, graph2_edges, states2, final_states["graph2"])
else:
    print("Bledne wejscie")
