class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashMap = dict()
        
        for i in s:
            print(i)
            hashMap[i] = 1 + hashMap.get(i, 0)
            
            if hashMap[i] == 2:
                return i


#super simple hashMap solution. Keeps count in the values as soon as the first one reach 2 then it returns current key            
