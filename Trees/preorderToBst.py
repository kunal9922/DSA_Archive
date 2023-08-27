import numpy as np
from isBST import isBST

class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.left, self.right = (None, None)

class Tree:
    def preorderToBstUtils(self, preorder: list, n: int, pos: int, curNode: Node, min_, max_) -> int:
        if pos == n or preorder[pos] < min_ or preorder[pos] > max_: #Boundary cases
            return pos
        if preorder[pos] < curNode.data: # Insert value in the left subtree
            curNode.left = Node(preorder[pos])
            pos += 1
            pos = self.preorderToBstUtils(preorder, n, pos, curNode.left, min_, curNode.data - 1)

        if pos == n or preorder[pos] < min_ or preorder[pos] > max_: # Checking Boundary cases again because the postion could have changed
            return pos
        # Inserting to the right subtree
        curNode.right = Node(preorder[pos])
        pos += 1
        return self.preorderToBstUtils(preorder, n, pos, curNode.right, curNode.data + 1, max_)

    def bstFromPreorder(self, preorder: list):
        if not preorder:
            return None # Preorder is empty
        rootNode = Node(preorder[0])
        if len(preorder) == 1:
            return rootNode
        else:
            self.preorderToBstUtils(preorder, len(preorder), 1, rootNode, float('-inf'), float('inf'))
        
        return rootNode
    
preArray = [8, 5, 1, 7, 10, 12]
bstTree = Tree()
myRoot = bstTree.bstFromPreorder(preArray)
print(isBST(myRoot))