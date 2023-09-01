class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Tree:
    def countTreeNodes(self, root: Node):
        if not root:
            return 0
        left_levels = 1
        l = root.left
        # traversing to the left most depth
        while(l):
            l = l.left
            left_levels += 1
        
        right_level = 1
        r = root.right
        # Traversing to the right most depth
        while(r):
            r = r.right
            right_level += 1
        # if it is a complete binary tree from the given root
        if left_levels == right_level:
            return 2 ** left_levels - 1
        
        # IF not count for left subtree as well as right subtree
        return 1 + self.countTreeNodes(root.left) + self.countTreeNodes(root.right)

# Example Binary tree:
#        4
#      /  \
#     2    7
#    / \  / 
#   1  3 6  
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)

# time complexity O(logN * logN)
binarTreeClf = Tree()
noOfNodes = binarTreeClf.countTreeNodes(root)
print(noOfNodes)