import random
import numpy as np
import pandas as pd
from numpy.linalg import matrix_power


def v_e_list(k):
    e = []
    v = np.arange(0, k, 1)
    while len(e) < k:
        a = random.choice(v)
        b = random.choice(v)
        if (a, b) not in e and a != b:
            e.append((a, b))
        elif (b, a) not in e and a != b:
            e.append((b, a))
    return v, e


def neighbour_matrix(e, k, typ):
    matrix = np.zeros(shape=(k, k))
    for i in range(k):
        for j in range(k):
            if typ == 'skierowany':
                if (i, j) in e:
                    matrix[i, j] = 1
                elif (j, i) in e:
                    matrix[j, i] = 1
            elif typ == 'nieskierowany':
                if (i, j) in e:
                    matrix[j, i] = 1
                    matrix[i, j] = 1
    return matrix


def incidence_matrix(v, e, typ):
    e = sorted(e)
    matrix = np.zeros(shape=(len(v), len(e)))
    if typ == 'nieskierowany':
        for i in v:
            for j, edge in enumerate(e):
                if i in edge:
                    matrix[i, j] = 1
    elif typ == 'skierowany':
        for i in v:
            for j, edge in enumerate(e):
                a, b = edge
                if i == a:
                    matrix[i, j] = 1
                if i == b:
                    matrix[i, j] = -1
    df = pd.DataFrame(matrix, index=v, columns=e)
    print(df)
    return matrix


def path_neigh(v, matrix, a, b):
    i = 1
    while i < len(v):
        res = matrix_power(matrix, i)
        if res[a, b] == 1:
            return i
        i += 1
    return -1


def check_integr(v, matrix):
    k = len(v)
    res = matrix_power(matrix, k)
    for i in range(k):
        if matrix[i].any() == 0:
            return False
    return True


k = 8
typ = 'nieskierowany'
v, e = v_e_list(k)
matrix = neighbour_matrix(e, k, typ)
print(e)
# incidence_matrix(v, e, typ)
print(path_neigh(e, matrix, 1, 3))
# print(check_integr(v, matrix))