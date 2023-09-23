class Solution:
    def maxWater(self, height: list[int]) -> int:
        """The code is implementing a solution to find the maximum amount of water that can be trapped
            between vertical lines represented by the `height` list."""
        if not height:
            return 0
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

s = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(s.maxWater(height))