# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid[0]),len(grid)
        max_island = 0
        def search(i,j):
            if i < 0 or i >= m or j < 0 or j >=n or grid[i][j] != 1:
                return 0
            grid[i][j]= -1
            return ( 1 + search(i+1,j) + search(i-1,j) + search(i,j+1) + search(i,j-1) )
        for i in range(m):
            for j in range(n):
                    max_island = max(max_island,search(i,j))
        return max_island