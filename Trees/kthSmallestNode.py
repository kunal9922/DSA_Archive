class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    def in_order_traversal(node):
        if not node:
            return []
        
        left = in_order_traversal(node.left)
        current = [node.val]
        right = in_order_traversal(node.right)
        
        return left + current + right
    
    elements = in_order_traversal(root)
    
    if 1 <= k <= len(elements):
        return elements[k - 1]
    else:
        return None


# Create a BST:
#        3
#       / \
#      1   4
#       \
#        2
root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)

k = 2
result = kthSmallest(root, k)
print(f"The {k}th smallest node in the BST is {result}")  # Output: The 2nd smallest node in the BST is 2
