from collections import deque
class Solution:
    def maxSlidingWindow(self, nums:list[int], k:int) -> list[int]:
        output = [] # store the results
        queue = deque() # it will store the indexes
        l = r = 0
        # Time O(n)
        while r < len(nums):
            # Maintain the decreasing order 
            while queue and nums[queue[-1]] < num[r]:
                queue.pop()
            queue.append(r)
            # Remove left val from window
            if l > queue[0]:
                queue.popleft()

            if (r + 1) >= k:
                output.append(nums[queue[0]])

            r += 1
        return output  
