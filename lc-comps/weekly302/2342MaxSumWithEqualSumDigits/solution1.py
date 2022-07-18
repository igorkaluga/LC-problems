class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hashSet = dict()
        
        maxNum = -1
        
        for j in nums:
            diff = sum([int(digit) for digit in str(j)])
            
            if diff not in hashSet:
                hashSet[diff] = j
            else:
                maxNum = max(maxNum, j + hashSet[diff])
                hashSet[diff] = max(j, hashSet[diff])
            
        
        return maxNum
