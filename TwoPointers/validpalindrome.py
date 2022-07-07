class Solution:
    def isPalindrome(self, s: str) -> bool:
        alph = "abcdefghijklmnopqrstuvwxyz01923456789"
        
        fixS = [x for x in s.lower() if x in alph]
        
        if len(fixS) == 0:
            return True
        
        s = 0
        e = len(fixS) - 1
        
        for i in fixS:
            if s > e or s == e:
                return True
            if fixS[s] == fixS[e]:
                s += 1
                e -= 1
            else:
                return False
