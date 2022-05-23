import numpy as np
import random


def arr2d(m, n):
    x = np.zeros(shape=(m, n))
    for i in range(m):
        for j in range(n):
            x[i][j] = random.randint(1, 9)
    return x


def sort_arr2d(x):
    y = len(x[0])
    for i in range(y-1, -1, -1):
        x = sorted(x, key=lambda p: p[i], reverse=True)
    return x


if __name__ == '__main__':
    x = arr2d(7, 8)
    sorted_x = sort_arr2d(x)
    for i in sorted_x:
        print(i)