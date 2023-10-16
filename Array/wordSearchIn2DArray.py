# Given m x n grid of characters find the path that matches the target word
class Solution:
    def isWordExists(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                word[i] != board[r][c] or
                (r, c) in path):
                return False
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res
        
        # Iterate over all the elements
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
                
        return False

# Time complexity O(n * m * 4^n)
s = Solution()
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'F']
]
targetWord = 'ABCCED'
result = s.isWordExists(board, targetWord)
print(result)
                
        