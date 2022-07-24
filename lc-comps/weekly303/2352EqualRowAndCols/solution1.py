class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ret = 0
        
        
        for i in range(len(grid)):
            compList = []
            vert = 0
            while vert < len(grid):
                compList.append(grid[vert][i])
                vert += 1
            
            ret += grid.count(compList)
                
        return ret

#The idea behind this solution is to go through the grid column by column and check if there exists a row by using grid.count thats the same as the column.
