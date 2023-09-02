class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)
        while l < r:
            if s[l] != s[r]:
                # Deleting a character and check is it still a palindrome
                skipL, skipR = s[l+1: r+1], s[l: r]
                return (skipL == skipL[::-1]
                        or skipR == skipR[::-1]) # Check still palindrome
            l, r = l + 1, r - 1
            return True