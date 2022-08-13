# Recursion Problems

""" Organizational Structure:
        - Problem name, link to where I found it  with its explanation, this will be a direct copy of Leetcode or whichever resource I state as it belonging to.  
        - Sample input and output, could include constraints.
        - Diagram that represents the solution with the actual code. The first solution will be mine, sometimes I will update newer solutions and very often will copy solutions that I will break down.
        - For each solution I will submit it and see how it matches up in that platform, do this 5 times, write down how much it changes between submissions, make an average and leave it with that score. The goal is to compare how the code matches up and also start developing a sense of where the code was losing time or gaining time, or when it used more memory or didnt required more.
        - I will write down how many tests it passed based on the submission data.

This will be repeated for some number of problems, not sure how many but likely a lot.

Contributors list:
        - Leetcode, thank you very much  for all the problems
""" 

'''695. Max Area of Island, https://leetcode.com/problems/max-area-of-island/ 

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
'''
'''Insights,        
        - I can use a 
        - I can change the 1 to 0 after the count , 
        
Diagramming + Logic,

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

VARIABLES:
    max_count = 0 
    local_count = 0

Output: 6

'''

class Solution(object):
    def maxAreaOfIsland(self, grid):
        
        # Solution from leet code submissions
        rows,cols = len(grid),len(grid[0])
        visit = set()
        def dfs(r,c):
            if(r<0 or r==rows or c<0 or c==cols or grid[r][c]==0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
        area=0
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]==1):
                    area = max(area,dfs(r,c))
        return area
        
        # Attempt 1 
        '''
        max_count = 0
        
        def helper(x, y, local_count):
            
            if grid[x][y] == None or grid[x][y] == 0:
                return 
            
            local_count += 1
            
            nonlocal max_count
            
            if local_count > max_count:
                max_count = local_count
            
            helper(x-1, y, local_count)
            helper(x+1, y, local_count)
            helper(x, y-1, local_count)
            helper(x, y+1, local_count)
            
            grid[x][y] = 0
                   
            #helper(grid_post[x-1][y],local_count)
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    helper(x, y, local_count=0)            
                
        return max_count
        '''
