# Breadth First search iterative using queue
from collections import deque


class Node:

    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children

    def bfs(self):
        queue = deque()
        queue.append(self)
        while len(queue) > 0:
            node = queue.popleft()
            print (node.data)

            if node.children != None:
                for child in node.children:
                    queue.append(child)


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    a.children = [b, c, d]
    b.children = [e, f]
    a.bfs()
