class Solution:
    def twoSum(self, nums: list[int], target: int) -> list:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            # otherwise we will add the current num
            prevMap[n] = i

obj = Solution()
print(obj.twoSum([2, 1, 5, 3], 4)) # time complexity O(n)