# Valid Sequence from root to leaf in a binary tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Tree:
    def __vaildSequenceFromRootToLeafUtils(self, root: Node, seq: list, pos) -> bool:
        if root.data != seq[pos] or pos == len(seq):
            return False
        left = None
        right = None
        if root.left:
            left = self.__vaildSequenceFromRootToLeafUtils(root.left, seq, pos + 1)
        if root.right:
            right = self.__vaildSequenceFromRootToLeafUtils(root.right, seq, pos + 1)
        
        if left or right:
            return True
        # If we reached to the leaf and sequence is ended
        if (root.left is None and root.right is None) and root.data == seq[-1]:
            return True
        # Could'n Find the sequence 
        return False
    def isValidSequence(self, root: Node, seq: list):
        return self.__vaildSequenceFromRootToLeafUtils(root, seq, 0) if root else False
    
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

binaryTreeClf = Tree()
print(binaryTreeClf.isValidSequence(root, [1, 2, 5]))