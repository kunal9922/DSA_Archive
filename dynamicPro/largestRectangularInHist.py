# find the Largest Rectangular Area in a Histogram Time complexity O(n), Space O(n)
class Solution:
    def largestRectangularArea(self, heights) -> int:
        '''Find the largest Rectangular in a histogram'''
        # No histogram has passed
        if len(heights) == 0:
            return 0
        
        size = len(heights)
        stack = []
        left = [0 for _ in range(size)]
        right = [0 for _ in range(size)]
        
        # filling the left 
        for i in range(size):
            if not stack:
                left[i] = 0 # till the left most index
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    stack.pop()
                left[i] = stack[-1] + 1 if stack else 0
                stack.append(i) 
        
        # Reuse the same stack by clearing it
        while stack:
            stack.pop()
        
        # Fill the right
        for j in range(size-1, -1, -1):
            if len(stack) == 0:
                right[j] = size - 1
                stack.append(j)
            else:
                while stack and heights[j] <= heights[stack[-1]]:
                    stack.pop()
                right[j] = stack[-1] - 1 if stack else size - 1
                stack.append(j)
        
        maxArea = 0 # Stores max Area
        for i in range(size):
            maxArea = max(maxArea, heights[i] * (right[i] - left[i] + 1))
        return maxArea

dp = Solution()
histogram = [2, 1, 5, 6, 2, 3]
print(dp.largestRectangularArea(histogram))
