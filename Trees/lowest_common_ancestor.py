class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def lowest_common_ancestor(self, root: Node, p: Node, q: Node):
        # values are present at the root
        if root.val == p.val or root.val==q.val:
            return root
        # Leaf node
        if not root.left and not root.right:
            return None
        # make calls
        left, right= None, None
        if root.left:
            left = self.lowest_common_ancestor(root.left, p, q)
        if root.right:
            right = self.lowest_common_ancestor(root.right, p, q)
        if left and right: # Found the lowest common ancestor
            return root
        # If a node to be a descendant of itself
        return right if left is None else left

binaryTree = Tree()
# Example tree:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

p = Node(4)
q = Node(5)

lca = binaryTree.lowest_common_ancestor(root, p, q)
print(lca.val)
# Time Complexity O(n)