class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        count = 0
        
        hashM = dict()
        #creates the hash map key - num, val - count
        for i in set(nums):
            hashM[i.bit_count()] = 1 + hashM.get(i.bit_count(), 0)

        for i in hashM:
            for j in hashM:
                if i + j >= k:
                    print(i,j)
                    count += hashM[i] * hashM[j]
                        
        return count

#https://leetcode.com/problems/number-of-excellent-pairs/
#uses a hashmap and binds bit count to keys and how many times that bit appears for the value. Iterates all possiilities with nested for loop and if the sum of bits >= k then update count by multiplying the values of hashM[i] and hashM[j]
