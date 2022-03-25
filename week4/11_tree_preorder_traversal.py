class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def preOrderRecursive(node, s):
    if node is None:
        return ""
    return (
        str(node.info)
        + " "
        + preOrderRecursive(node.left, s)
        + preOrderRecursive(node.right, s)
    )


def preOrderOld(root):
    """
    Simplest to write but not the best: use recursion
    """
    s = ""
    print(preOrderRecursive(root, s))


from collections import deque


def preOrder(root):
    """
    Better: use a queue or stack.
    """
    queue = deque()
    queue.append(root)
    result = ""
    while queue:
        current_node = queue.pop()
        if current_node is not None:
            result += str(current_node.info)
            result += " "
            queue.append(current_node.right)
            queue.append(current_node.left)
    print(result)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)
