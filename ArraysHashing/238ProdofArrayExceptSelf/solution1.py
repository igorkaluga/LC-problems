class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        preNum = 1
        for i in range(len(nums)):
            res[i] *= preNum
            preNum *= nums[i]
            
        postNum = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postNum
            postNum *= nums[i]
            
        return res
            
