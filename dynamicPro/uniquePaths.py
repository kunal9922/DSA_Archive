class Solution:
    def uniquePaths(self, m: int, n: int):
        '''Find the unique way to reach the end from the start of the matrix
        Time Complexity O(mn)'''
        grid = [
            [0 for _ in range(n)]
        ] * m
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0: # We are at the boundary of the grid
                    grid[i][j] = 1
                else: # Calculate the distance
                    grid[i][j] = grid[i-1][j] + grid[i][j-1] # Up and Left move in DP tabulation
        
        return grid[m-1][n-1]
    
dp = Solution()
paths = dp.uniquePaths(3, 4)
print(paths)

