class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, highest = prices[0], prices[0]
        sale = 0
    
        for i in prices:
            if i < lowest:
                lowest = i
                highest = 0
            elif i > highest:
                highest = i
                
            if highest - lowest > sale:
                sale = highest - lowest
                
        return sale
        
