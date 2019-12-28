# Depth first search both recursive and iterative(Using Stacks)

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

    def dfs_iterative(self):
        stack = []
        stack.append(self)
        while len(stack) > 0:
            node = stack.pop()
            print (node.data)
            if node.children != None:
                stack += reversed(node.children)


class Solution:
    def dfs(self, root):
        def helper(node):
            if not node:
                return
            print(node.data)
            if node.children:
                for child in node.children:
                    helper(child)

        return helper(root)

    def dfs_Iterative(self, root):

        stack = []
        stack.append(root)
        while len(stack):
            node = stack.pop()
            print(node.data)
            if node.children:
                stack += reversed(node.children)


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    a.children = [b, c, d]
    b.children = [e, f]
    # a.dfs()
    # a.dfs_iterative()
    # Solution().dfs(a)
    Solution().dfs_Iterative(a)
