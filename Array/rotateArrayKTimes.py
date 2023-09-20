class Array:
    def rotateArray(self, nums:list[int], k:int) -> None:
        """Rotate an array a given number of times in place space O(1).
        Args:
            nums (list[int]): input Array of number
            k (int): number of times to rotate the array
        """        
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            # Reverse the entrire array once
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # revese the array from the beginning to the k-th position
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        # reverse the array from the k-th position to the end
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]

arr = Array()

arr.rotateArray(testArray, 3)
print(testArray)