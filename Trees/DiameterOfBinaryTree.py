# Diameter of a binary tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __diameter_of_binary_tree_utils(self, root: Node):
        if root is None:
            return [0, 0]
        left: list = self.__diameter_of_binary_tree_utils(root.left)
        right: list = self.__diameter_of_binary_tree_utils(root.right)

        internal_path = max(left[1], right[1])
        if left[0] + right[0] + 1 > internal_path:
            internal_path = left[0] + right[0] + 1
        return [max(left[0], right[0]) + 1, internal_path]
    
    def diameter_of_binary_tree(self, root: Node):
        '''Find the Diameter of a Binary Tree'''
        if root is None:
            return 0
        result = self.__diameter_of_binary_tree_utils(root)
        return max(result[0], result[1]) - 1

# Example Binary tree:
#       1
#      / \
#     2   3
#    / \   
#   4   5   
#        \
#         6  
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)

# Time Complexity is O(n)
binaryTree = Tree()
diameterOfBinaryTree = binaryTree.diameter_of_binary_tree(root)
print(diameterOfBinaryTree)