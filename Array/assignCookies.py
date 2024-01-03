class AssignCookies:
    def findContentChildren(self, g:[int], s:[int]) -> int:
        g.sort()
        s.sort()

        i = j = 0
        # Find the content children
        while i < len(g):
            while j < len(s) and g[i] > s[j]: # finding out the bigger cookie to accomplish the child's greed
                j += 1
            if j >= len(s):
                break
            i += 1
            j += 1
        # Return the content children
        return i

ac = AssignCookies()
print(ac.findContentChildren([1, 2, 3], [1, 1]))