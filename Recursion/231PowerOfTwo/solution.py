class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        else:
            if n == 1 or (n % 2 == 0 and self.isPowerOfTwo(n / 2)):
                return True
