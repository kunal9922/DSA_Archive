class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Last index is nums1 
        last = m + n - 1
        
        #  merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        
        # Fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            n , last = n - 1, last - 1
            
arr1 = [1, 2, 3, 0, 0, 0]
arr2 = [2, 5, 6]

s = Solution()
s.merge(arr1, 3, arr2, 3)
print(arr1)

# Time complexity O(n) Space complexity O(1)
