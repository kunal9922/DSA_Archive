# Edge case would be '*' can be considered as '' or '(' or ')'
class Solution:
    def checkValidString(self, inputString) -> bool:
        openStack, starStack = [], []
        lenStr = len(inputString)
        
        for i in range(lenStr):
            if inputString[i] == '(':
                openStack.append(i)
            elif inputString[i] == '*':
                starStack.append(i)
            else:
                if openStack:
                    openStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False 
                     
        # Now process leftover opening brackets
        while openStack:
            if not starStack:
                return False
            elif openStack[-1] < starStack[-1]:
                openStack.pop()
                starStack.pop()
            else:
                return False
            
        return True
    
s = Solution()
# Valid (*), (*)), *())
# Invalid )*()
print(s.checkValidString('*(()*))'))