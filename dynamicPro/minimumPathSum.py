class Solution:
    def minPathSum(self, grid) -> int:
        rows = len(grid)
        # if grid is empty 
        if rows == 0:
            return 0
        cols = len(grid[0])
        # Creating a DP table for storing minimum path sum 
        dp = grid[::]
        # Fill the first Row
        for i in range(1, cols):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        # Fill the first column
        for j in range(1, rows):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        
        # Now fill the rest of the cell
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
            
        return dp[rows-1][cols-1]

dp = Solution()
grid = [
    [1, 3, 5],
    [2, 1, 2],
    [4, 3, 1]
]
minPath = dp.minPathSum(grid)
print(minPath)