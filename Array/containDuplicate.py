class Solution:
    def containDuplicate(self, nums: list[int]) -> bool:
        unique = set()

        for n in nums:
            if n in unique:
                return True
            else:
                unique.add(n)
        
        return False

arrQ = Solution()
hasDuplicate = arrQ.containDuplicate([1,2,3,4,3])
print(hasDuplicate)