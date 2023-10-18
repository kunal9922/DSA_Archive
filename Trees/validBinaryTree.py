class Solution:
    def validateBinaryTree(self, n, leftChild, rightChild) -> bool:
        """The function checks if a given binary tree is a valid tree """
        hasParent: set = set(leftChild + rightChild)
        hasParent.discard(-1) # Discard -1 once 
        
        if len(hasParent) == n:
            return False
        
        root = -1
        # find the parent node
        for i in range(n):
            if i not in hasParent:
                root = i # find out the parent node
                break
        
        visit = set()
        def dfs(i):
            '''For Cycle detection in the Binary Tree'''
            if i == -1:
                return True
            if i in visit:
                return False
            visit.add(i)
            return dfs(leftChild[i]) and dfs(rightChild[i])
        
        return dfs(root) and len(visit) == n
    
# Time complexity O(n) Space complexity O(n)
'''input: n = 4, leftChild = [1, -1, 3, -1], rightChild = [2, -1, -1, -1]
output: True'''
'''
    0
   /  \
  1    2
      /
     3 
'''
s = Solution()
result = s.validateBinaryTree(4, [1, -1, 3, -1], [2, -1, -1, -1])
print(result)