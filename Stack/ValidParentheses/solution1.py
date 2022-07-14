class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pDict = {")":"(", "}":"{", "]":"["}
        
        p = -1
        for c in s:
            if c not in pDict:
                stack.append(c)
                p += 1
            elif c in pDict and pDict[c] in stack and pDict[c] == stack[p]:
                stack.pop()
                p -= 1
            else:
                return False
            
        return p == -1
        
        
        
