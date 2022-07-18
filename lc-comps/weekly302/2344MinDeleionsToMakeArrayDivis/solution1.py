class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        ret = 0
    
        newNums = sorted(nums)
        minVal = newNums[0]
        
        i = 0
        while i < len(numsDivide):
            if numsDivide[i] % minVal == 0:
                i += 1
            else:
                oldNumsLen = newNumsLen = len(newNums)
                removeK = newNums[0]
                for k in newNums:
                    if k == removeK:
                        newNums.pop(0)
                        newNumsLen -= 1
                    else:
                        break
                ret += oldNumsLen - newNumsLen
                if newNumsLen != 0:
                    minVal = newNums[0]
                    i = 0
                else:
                    return -1
                
        return ret

# Not the best way to do this prob but I wanted to work through
# the idea that I had in my head to see if it was possible.
# Kept getting TLE error so I sorted the array first to make the min
# value always be the 0th index of the newNums array.
# Before I used list comprehension to remove the unwanted nums.
