class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pDict = {")":"(", "}":"{", "]":"["}
        
        for c in s:
            if c in pDict:
                if stack and pDict[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False
        
        
#https://www.youtube.com/watch?v=WTzjTskDFMg variation after watching this solution
