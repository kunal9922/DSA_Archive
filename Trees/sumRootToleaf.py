class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
class Tree:
    ans = 0
    def dfs(self, root: Node, val):
        if root is None:
            return
        #left shift the value
        val *= 10
        val += root.data
        if root.left is None and root.right is None:
            self.ans+=val
            return
        self.dfs(root.left, val)
        self.dfs(root.right, val)

    def sum_root_to_leaf(self, root: Node):
        if root is None:
            return self.ans
        self.dfs(root, 0)
        return self.ans
    
# Example tree:
#       8
#      / \
#     2   9
#    / \   \
#   4   7   10
root = Node(8)
root.left = Node(2)
root.right = Node(9)
root.left.left = Node(4)
root.left.right = Node(7)
root.right.right = Node(10)

binaryTree = Tree()
sumof = binaryTree.sum_root_to_leaf(root)
print(sumof)