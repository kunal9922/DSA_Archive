# Check weather the string is valid parentheses 
class ValidString:
    def checkBalancedParentheses(self, inputString: str) -> bool:
        n = len(inputString)
        # Create a stack of valid parentheses
        stack = [] 
        for i in range(n):
            if inputString[i] in ['(', '{', '[']:
                stack.append(inputString[i])
            elif inputString[i] in [')', '}', ']']:
                if not stack:
                # Top doesn't pair with inputString[i]
                    return False
                else:
                    stack.pop()
        
        return False if stack else True
    
nameCheck = ValidString()
validOrNot = nameCheck.checkBalancedParentheses("{kunal}[soni]{{(()}}")
print(validOrNot)