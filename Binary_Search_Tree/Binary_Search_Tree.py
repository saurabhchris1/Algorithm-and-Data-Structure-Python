class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(node):
    if node is None:
        return

    print(node.data)
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data)
    inorder(node.right)


def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data)


def search(node, value):
    if node is None:
        return False

    if value == node.data:

        return True
    elif value > node.data:

        return search(node.right, value)
    else:

        return search(node.left, value)


if __name__ == "__main__":
    node = Node(10)
    node.left = Node(5)
    node.right = Node(40)
    node.right.right = Node(50)
    node.left.left = Node(1)
    node.left.right = Node(7)

    print ("This is preorder : ")
    preorder(node)
    print ("This is postorder : ")
    postorder(node)
    print ("This is inorder : ")
    inorder(node)

    print(search(node, 2))
    print (search(node, 7))
