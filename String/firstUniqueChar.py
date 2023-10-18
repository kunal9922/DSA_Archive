class Solution:
    def firstUniqueChar(self, string: str) -> int:
        n = len(string)
        freq = [0 for _ in range(26)]
        
        # store the frequency of the characters
        for i in range(n):
            freq[ord(string[i]) - ord('a')] += 1
            
        # Now Traverse and find the first non-repeating char
        for i in range(n):
            if freq[ord(string[i]) - ord('a')] == 1:
                return i
            
        # All characters are repeating
        return -1
        
s = Solution()
print(s.firstUniqueChar('techtricks'))     