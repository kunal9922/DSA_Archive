class Solution:
    def maximumSqaureArea(self, grid: list[list]) -> int:
        rows = len(grid)
        if rows == 0: # Matrix is empty
            return 0
        cols = len(grid[0])
        dp = [
            [0 for _ in range(cols+1)]
        ] * (rows + 1)

        largest = 0
        # process all the elements of matrix
        for i in range(1, rows):
            for j in range(1, cols):
                if grid[i-1][j-1] == 1:
                    dp[i][j] = 1 + min(
                        dp[i-1][j], dp[i][j-1], dp[i-1][j-1]
                    )
                    if largest < dp[i][j]:
                        largest = dp[i][j]
        
        return largest * largest

orignalGrid = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]
dpForMatrix = Solution()
areaOfLargestSqaure = dpForMatrix.maximumSqaureArea(orignalGrid)
print(areaOfLargestSqaure)
