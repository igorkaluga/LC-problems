class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        i, j = 0, len(height) - 1 # left and right pointers
        maxLeft, maxRight = 0, 0
        maxIndex = height.index(max(height))
        
        while i < j:
            curI = height[i]
            curJ = height[j]
            
            if curI > maxLeft: 
                maxLeft = curI
            if curJ > maxRight:
                maxRight = curJ
                
            if curI < maxLeft:
                water += maxLeft - curI
            if curJ < maxRight:
                water += maxRight - curJ
                
            if i != maxIndex:
                i += 1
            if j != maxIndex:
                j -= 1
        
        return water
