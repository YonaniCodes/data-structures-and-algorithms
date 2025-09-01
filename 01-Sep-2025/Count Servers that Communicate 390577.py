# Problem: Count Servers that Communicate - https://leetcode.com/problems/count-servers-that-communicate/description/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)            
        n = len(grid[0])        
        Rcount = [0]*n        
        Ccount = [0]*m       
        
 
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    Rcount[j] += 1
                    Ccount[i] += 1

        res = 0
        
        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    if Rcount[col] > 1 or Ccount[row] > 1:
                        res += 1
        return res
