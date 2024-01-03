class Solution:
    def hammingDistance(self, x:int, y:int)->int:
        xorVal = x ^ y
        countSetBits = 0
        
        while xorVal:
            if xorVal & 1:
                countSetBits += 1
            xorVal >>= 1
        return countSetBits

bitManipular = Solution()
print(bitManipular.hammingDistance(1, 4))