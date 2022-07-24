class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        count = 0
        
        skipArr = []
        skipPair = []
        
        for i in nums:
            iBit = i.bit_count()
            if nums.count(i) >= 1:
                if i.bit_count() * 2 >= k and i not in skipArr:
                    skipArr.append(i)
                    count += 1
            for j in nums:
                jBit = j.bit_count()
                if [i,j] not in skipPair and [j,i] not in skipPair:
                    if iBit + jBit >= k and i != j:
                        skipPair.append([i,j])
                        count += 2
                        
                        
        return count
      
#Originally I was trying to make this solution work but it returns TLE error for large inputs.
#This is why in the passing solution using a hash table is a lot quicker.
