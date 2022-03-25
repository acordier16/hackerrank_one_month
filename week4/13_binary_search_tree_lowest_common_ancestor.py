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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''

from collections import deque
from copy import copy

def get_path_for_queried_value(root, v):
  """
  Given a queried value, will return the path (as a list of nodes)
  to the node corresponding to the queried value.
  """
  queue = deque()
  queue.append((root, [])) # Each element in the queue is (node, path)
  while queue:
    node, path = queue.pop()
    if node is not None:
        new_path = copy(path)
        new_path.append(node)
        # If we found the value, we return its path
        if node.info == v:
            return new_path
        queue.append((node.right, new_path))
        queue.append((node.left, new_path))

def lcaAnyTree(root, v1, v2):
  """
  Note that this code actually works for any tree rather than for a BST.
  What this does is that it will search for v1 and build its path, and then search for
  v2 and build its path. Then we compare the paths.
  """
  path_v1 = get_path_for_queried_value(root, v1)
  path_v2 = get_path_for_queried_value(root, v2)
  lca = root
  for i in range(min(len(path_v1), len(path_v2))):
    if path_v1[i].info == path_v2[i].info:
        lca = path_v1[i]
    else:
        break
  return lca

def lca(root, v1, v2):
    """
    This code works for BST only, but is more optimal.
    A binary search tree (BST), also called an ordered or sorted binary tree,
    is a rooted binary tree data structure whose internal nodes each store a key
    greater than all the keys in the node's left subtree and less than those in its right subtree.
    It is fairly easy to see that the LCA of two values will always be the first node with a value
    in-between the two queried values.
    Note that all values are distinct in a BST.
    This code is in O(log(n)), and could therefore also be written recursively safely with same time complexity.
    """
    node = root
    v1, v2 = min(v1, v2), max(v1, v2) # v1 = lower bound, v2 = higher bound
    while not (node.info >= v1 and node.info <= v2):
        if node.info < v1:
            node = node.right
        elif node.info > v2:
            node = node.left
    return node



tree = BinarySearchTree()
