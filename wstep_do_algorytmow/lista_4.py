# %%
from queue import Queue as q
from typing import Type, Union
import copy


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class LinkedList():
    value = None
    next_value: Union[Type["LinkedList"], None]

    def __init__(self, fpvalue):
        self.value = fpvalue
        self.next_value = None

    def __iter__(self):
        self.iter = self
        return self

    def __next__(self):
        if self.iter is None or not self.iter.length():
            raise StopIteration
        x = self.iter
        self.iter = self.iter.next_value
        return x

    def last(self):
        current = self
        while True:
            if current.next_value is None:
                break
            current = current.next_value
        return current

    def length(self):
        current = self
        if self.value is None and self.next_value is None:
            return 0
        i = 1
        while True:
            if current.next_value is None:
                break
            current = current.next_value
            i += 1
        return i


class Stack(LinkedList):
    def push(self, item: 'LinkedList'):
        if self.value is None and self. next_value is None:
            self.value = item.value
            self.next_value = item.next_value
            return
        self.last().next_value = item

    def pop(self):
        if not self.length():
            return None
        if self.next_value is None:
            item = copy.copy(self)
            self.value = None
            return item
        stl = self
        for _ in range(self.length() - 2):
            stl = stl.next_value
        item = stl.next_value
        stl.next_value = None
        return item


def visit(x):
    print(x, end='')


def bfs(top, visit):
    if top is None:
        return
    queue = q()
    queue.put(top)
    while not queue.empty():
        node = queue.get()
        visit(node)
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)


def dfs(top, visit):
    if top is None:
        return
    stack = Stack(top)
    while element := stack.pop():
        node = element.value
        visit(node)
        if node.right:
            stack.push(Stack(node.right))
        if node.left:
            stack.push(Stack(node.left))


def find_path(root, fpvalue, path=Stack(None)):
    node = root
    path.push(Stack(node))
    if node.data == fpvalue:
        return path
    if node.left:
        jk = find_path(node.left, fpvalue, path)
        if jk is not None:
            return jk
        path.pop()
    if node.right:
        jk = find_path(node.right, fpvalue, path)
        if jk is not None:
            return jk   
        path.pop()
    return None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

print('wyszukiwanie wszerz:')
bfs(root, visit)
print('\nwyszukiwanie wglab:')
dfs(root, visit)
# %%
new_root = int(input('\nPodaj nowy korzeń (liczba od 4 do 7): '))
new_root = rotate_tree(root, new_root)
bfs(new_root, visit)
# %%
