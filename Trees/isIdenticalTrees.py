class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Trees:
    def isIdentical(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True # We've traversed till the leaf node and trees are identical
        if not p or not q or p.val != q.val:
            return False # Trees are identical
        
        return self.isIdentical(p.left, q.left) and self.isIdentical(p.right, q.right)
    
# Time complexity O(p + q)
# Example Binary tree 1:
#       4
#      / \
#     2   7
#    / \   \
#   1   3   6
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(7)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(6)

# Example Binary tree 2:
#       6
#      / \
#     2   7
#    / \   \
#   1   5   6
root2 = TreeNode(6)
root2.left = TreeNode(2)
root2.right = TreeNode(7)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(5)
root2.right.right = TreeNode(6)

tree = Trees()
result = tree.isIdentical(root1, root2)
print(result)