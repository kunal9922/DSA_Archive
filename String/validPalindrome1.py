class Solution():
    def validPalinDrome1(self, s: str) -> bool:
        # Brute force With Extra Space O(n)
        newStr = "" # Storing the palindrome String

        for c in s:
            if c.isalpha():
                # Appending charcter to the palindrome string
                newStr += c
            
        return newStr == newStr[:: -1]

    def alphaNum(self, c):
        return 'a'<= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9'
        

    def validPalinDromeOpti(self, s: str) -> bool:
        # optimized Solution without Extra space
        l , r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        # String is a palindrome
        return True
    
strS = Solution()
testString = "Jakaj"
result = strS.validPalinDromeOpti(testString)
print(result)