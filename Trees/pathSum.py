class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # For Traversal on the tree 
        def dfs(node: TreeNode, currentSum: int):
            if currentSum > targetSum:
                return False
            elif not node:
                return False
            elif currentSum == targetSum:
                return True
            currentSum += node.val
            return (dfs(node.left, currentSum) or dfs(node.right, currentSum))
        
        return dfs(root, 0)
# Example Binary tree:
#       4
#      / \
#     2   7
#    / \   \
#   1   3   6
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(6)

targetSum = 9
s = Solution()
print(s.hasPathSum(root, targetSum))