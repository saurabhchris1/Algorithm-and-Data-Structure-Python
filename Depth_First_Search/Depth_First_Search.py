# Depth first search both recursive and iterative

class Node:

    def __init__(self, data=None, children=None):

        self.data = data
        self.children = children

    def dfs(self):

        self._dfshelper(self)

    def _dfshelper(self, node):

        print (node.data)

        if node.children != None:
            for child in node.children:
                self._dfshelper(child)


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    a.children = [b, c, d]
    b.children = [e, f]
    a.dfs()
