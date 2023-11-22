# Given two sorted arrays find the median value
class Solution():
    def findMedian(self, arr1: list[any], arr2: list[any]) -> int:
        '''Two pointer approach'''
        # find the length of the arrays
        l1 = len(arr1)
        l2 = len(arr2)
        midIdx = (l1 + l2) // 2

        # then we will skip the left over arrays elements
        count = 0
        p1, p2 = 0, 0 # two pointers to track the values
        while count <= midIdx and p1 < l1 and p2 < l2:
            if count == midIdx:
                break # found the median
            elif arr1[p1] <= arr2[p2]:
                p1 += 1
            elif arr1[p1] > arr2[p2]:
                p2 += 1
            count += 1
        
        return min(arr1[p1], arr2[p2]) # Return the median value

arr1 = [2, 4, 5]
arr2 = [3, 6, 9, 10]

s = Solution()
print(s.findMedian(arr1, arr2))
    