import random
import matplotlib.pyplot as plt
import networkx as nx
from robots import *


def robots_bst(robot_list, param):
    robots_dicts = []
    for i in robot_list:
        robots_dicts.append(i.save_robot())
    robots_tree = Node(robots_dicts[0][param], robots_dicts[0])
    for i in range(len(robots_dicts) - 1):
        robots_tree.insert(Node(robots_dicts[i + 1][param], robots_dicts[i + 1]))
    return robots_tree


class Node:
    def __init__(self, param=None, data=None, parent=None, left=None, right=None):
        self.param = param
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def preorder(self):
        print(self.param)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.param)
        if self.right is not None:
            self.right.inorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.param)

    def search(self, k):
        x = self
        while x is not None and k != x.param:
            if k < x.param:
                x = x.left
            else:
                x = x.right
        return x

    def min(self):
        x = self
        while x.left is not None:
            x = x.left
        return x

    def max(self):
        x = self
        while x.right is not None:
            x = x.right
        return x

    def next_node(self):
        if self.right is not None:
            return self.right.min()
        x = self
        y = self.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def prev_node(self):
        if self.left is not None:
            return self.left.min()
        x = self
        y = self.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y

    def insert(self, z):
        y = None
        x = self
        while x is not None:
            y = x
            if z.param < x.param:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is not None:
            if z.param < y.param:
                y.left = z
            else:
                y.right = z

    def remove(self, z):
        x = self
        if z.left is None or z.right is None:
            y = z
        else:
            y = z.succ()
        if y.left is not None:
            x = y.left
        else:
            x = y.right
        if x is not None:
            x.parent = y.parent
        if y.parent is not None:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        if y is not z:
            z.param = y.param
            z.data = y.data

    def get_path_label(self, path, res):
        if self.left is not None:
            self.left.get_path_label(path + 'l', res)
        if self.right is not None:
            self.right.get_path_label(path + 'r', res)
        res[path] = self.param

    def get_depth(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is not None and self.right is None:
            return self.left.get_depth() + 1
        elif self.left is None and self.right is not None:
            return self.right.get_depth() + 1
        else:
            return max(self.left.get_depth(), self.right.get_depth()) + 1

    def show_graph(self):
        G = nx.Graph()
        depth = self.get_depth()
        paths = {}
        pos = {}
        self.get_path_label('', paths)
        for path, value in paths.items():
            G.add_edge(path[:-1], path)
            n = 0
            x = 0
            for p in path:
                n += 1
                x += 2 ** (depth - n - 1) * (-1 if p == 'l' else 1)
            pos[path] = [x, -n / 2]
        G.remove_edge('', '')
        nx.draw(G, pos, labels=paths, with_labels=True)
        plt.show()


if __name__ == "__main__":
    robots = m_robots(10)
    tree = robots_bst(robots, 'zas')
    tree.show_graph()