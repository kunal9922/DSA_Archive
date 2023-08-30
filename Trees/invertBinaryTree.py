class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def dfs(self, root: Node):
        if root is None:
            return None
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        #Exchange the nodes
        root.left = right
        root.right = left
        return root

    def invert_binary_tree(self, root: Node):
        if root is None:
            return None
        return self.dfs(root)
        

# Example Binary tree:
#       4
#      / \
#     2   7
#    / \   \
#   1   3   6
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(6)

# Invert the tree (Time Complexity O(n))
binaryTree = Tree()
root = binaryTree.invert_binary_tree(root)

print(root.left.left.val) # 6 