import numpy as np
import math


def distance_between_nodes(v, w):
    return math.sqrt(pow(pos[v][0] - pos[w][0], 2) + pow(pos[v][1] - pos[w][1], 2))


def dist(v, w):
    dict_len = []
    neighbours = []
    length = 0
    if(v, w) in E or (w, v) in E:
        length = distance_between_nodes(v, w)
        dict_len.append(length)
    else:
        V.remove(v)
        for e in E:
            if v in list(e):
                for n in list(e):
                    if n != v and n in V:
                        neighbours.append(n)
        length = min([distance_between_nodes(v, i) + dist(i, w) for i in neighbours], default=np.infty)
    return length


V = ['a', 'b', 'c', 'd', 'e']
E = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'a')]
pos = {'a': (0, 0),
       'b': (1, 0),
       'c': (2, 1),
       'd': (1, 3),
       'e': (0, 1)}

print(dist('a', 'c'))
