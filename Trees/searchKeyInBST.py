class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class BST:
    def searchBST(self, root: Node, key):
        curNode: Node = root
        while curNode:
            if curNode.data == key:
                return curNode
            elif(curNode.data > key):
                curNode = curNode.left
            else:
                curNode = curNode.right
        
        return curNode
# Example tree:
#       5
#      / \
#     3   8
#    / \   \
#   2   4   9
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(9)

tree = BST()
whichSubtree = tree.searchBST(root, 8)
print(whichSubtree.data)