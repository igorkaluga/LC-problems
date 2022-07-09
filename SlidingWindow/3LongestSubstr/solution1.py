class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        l = maxCount = 0
        charSet = set()
        
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l]) # keep decreasing until you get to s[i]
                l += 1
            charSet.add(s[i]) #begin adding if not in charSet
            maxCount = max(maxCount, len(charSet))
        
        return maxCount
        
            
        
