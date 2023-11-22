class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        '''Returns if the given root is symmetric'''
        def dfs(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False # Trees are not symmetric
            
            return (left.val == right.val  
                    and dfs(left.left, right.right)
                    and dfs(left.right, right.left))
        
        return dfs(root.left, root.right)
# Example of the Symmetric Tree
#        4
#      /   \
#     2     2
#    / \   / \
#   1   3 3   1
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
root1.right.left = TreeNode(3)
root1.right.right = TreeNode(1)

s = Solution()
print(s.isSymmetric(root1))
