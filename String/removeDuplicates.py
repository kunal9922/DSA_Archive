def removeDuplicate(string: str) -> str:
    # sourcery skip: hoist-statement-from-loop
    '''Remove duplicate alphabets from a string'''
    alphaFreq = [0] * 26
    # filling the frequncies of charter occurancy
    for char in string:
        alphaFreq[ord[char] - ord['a']] += 1

    stack = []
    # visited character array to keep the track of characted has visited or not
    seen = [False] * 26

    for char in string:
        if seen[ord[char] - ord['a']] is True:
            # Don't process already included
            alphaFreq[ord[char] - ord['a']] -= 1
            continue
        # Otherwise pop all the possible larger chars
        while stack and stack[-1] > char and alphaFreq[ord[char] - ord['a']] > 0:
            seen[ord[char] - ord['a']] = False
            stack.pop()
        
        stack.append(char)
        seen[ord[char] - ord['a']] = True
        alphaFreq[ord[char] - ord['a']] -= 1
    
    ans = ''
    while stack: # Building answer string
        ans = ans + stack.pop()
    
    return ans[::-1] # Reverse the stack output

myInput = 'bcab'
print(removeDuplicate(myInput))
            