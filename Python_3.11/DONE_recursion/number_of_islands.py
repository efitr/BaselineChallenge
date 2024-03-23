'''Insights,
        - I should iterate through every single position within the matrix
            if I find a 1, it should go into a recursive call, that checks every position, up, down, left, right
                if the value exceeds or is less than the grid, dont go there
                color to 0 every place I find a 1
                add + 1 only once, when I find a 1
                The double loop wont notice


Diagramming + Logic,


'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def helper(x,y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return
            
            elif grid[x][y] == "0":
                return
            
            if grid[x][y] == "1":
                grid[x][y] = "0"
            
                helper(x-1,y)
                helper(x,y-1)
                helper(x+1,y)
                helper(x,y+1)
            
        num_island = 0
        
        for x in range(len(grid)):
            
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    num_island += 1
                    helper(x,y)
                    
        return num_island
