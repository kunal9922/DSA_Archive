# Using memoization to calculate
class Solution:
    def climbStairsRecursive(self, n, memo = {}):
        if n in memo: # Already calculated 
            return memo[n]
        
        if n <= 2:
            return n
        # Now taking 1 step and 2 step
        memo[n] = self.climbStairRecursive(n - 1, memo) + self.climbStairRecursive(n - 2, memo)
        return memo[n]
    
clmS = Solution()
n = 5
numOfSteps = clmS.climbStairRecursive(n)
print(f"Number of distinct ways to climb {n} stairs: {numOfSteps}")