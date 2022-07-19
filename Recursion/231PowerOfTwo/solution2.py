class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        k = power = 0
        
        while power < n:
            powerNum = 2 ** k
            if powerNum == n:
                return True
            else:
                power = powerNum
                k += 1
                
        return False

#iterative approach
