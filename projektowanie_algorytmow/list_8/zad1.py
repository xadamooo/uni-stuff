import copy
import networkx as nx
import matplotlib.pyplot as plt
import random

def partition(arr, low, high):
    """Metoda pomocnicza do quick sort - największa wartość wybierana jest jako pivot"""
    piv = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= piv:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i, arr


def quick_sort(arr, low, high):
    """Algorytm quick sort"""
    if low > high or low < 0:
        return
    p, arr = partition(arr, low, high)
    quick_sort(arr, low, p - 1)
    quick_sort(arr, p + 1, high)
    return arr


def check_bst(root):
    """Sprawdzenie czy drzewo spelnia warunki BST"""
    if root is None or (root.left is None and root.right is None):
        return True
    # przy takiej implementacji Node jesli jestesmy na koncu to nie mozemy sprawdzic val od Node
    #  bo w Pythonie var None nie posiada "atrybutow" dlatego ponizsze sprawdzenia
    elif root.right is None:
        return root.left.value < root.value and check_bst(root.left)
    elif root.left is None:
        return root.right.value >= root.value and check_bst(root.right)
    return check_bst(root.left) and check_bst(root.right)


def bst_parted(nodes, parent, direction):
    """Ustalanie rodzica z posortowanego, dzielonego na pół wektora wierzchołków"""
    n = len(nodes)
    if n > 0:
        if direction == 'l':
            parent.left = Node(nodes[n // 2], parent)
            bst_parted(nodes[:n // 2], parent.left, 'l')
            bst_parted(nodes[n // 2 + 1:], parent.left, 'r')
        else:
            parent.right = Node(nodes[n // 2], parent)
            bst_parted(nodes[:n // 2], parent.right, 'l')
            bst_parted(nodes[n // 2 + 1:], parent.right, 'r')


def bst_from_list(nodes):
    """Utworzenie drzewa binarnego z wektora wierzchołków"""
    n = len(nodes)
    nodes = quick_sort(nodes, 0, len(nodes) - 1)
    root = Node(nodes[n//2])
    bst_parted(nodes[:n//2], root, 'l')
    bst_parted(nodes[n//2 + 1:], root, 'r')
    return root


class Node:
    """Struktura przechowująca pojedynczy wierzchołek - przez odwołanie do rodzica
       i synów mamy jednocześnie strukturę drzewa binarnego"""
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def visualize(self):
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

    def get_path_label(self, path, res):
        if self.left is not None:
            self.left.get_path_label(path + 'l', res)
        if self.right is not None:
            self.right.get_path_label(path + 'r', res)
        res[path] = self.value

    def insert(self, z):
        y = None
        x = self
        while x is not None:
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is not None:
            if z.value < y.value:
                y.left = z
            else:
                y.right = z

    def remove(self, z):
        x = self
        if z.left is None or z.right is None:
            y = z
        else:
            y = z.next_node()
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
            z.value = y.value

    def repair_node(self, z):
        y = copy.copy(z)
        self.remove(z)
        self.insert(Node(y.value, None, None, None))

    def get_depth(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is not None and self.right is None:
            return self.left.get_depth() + 1
        elif self.left is None and self.right is not None:
            return self.right.get_depth() + 1
        else:
            return max(self.left.get_depth(), self.right.get_depth()) + 1


if __name__ == "__main__":
    # tree = Node(15)
    # for _ in range(10):
    #     num = random.randint(1, 30)
    #     tree.insert(Node(num))
    # tree.visualize()

    lst = [1, 3, 6, 11, 23, 14, 33, 19, 8]
    tree = bst_from_list(lst)
    tree.visualize()
    tree.repair_node(Node(6))
    tree.visualize()