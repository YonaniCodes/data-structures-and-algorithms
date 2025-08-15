# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self,matrix: List[List[int]]) -> int:
        n = len(matrix)
        
    
        dp = [row[:] for row in matrix]
        
    
        for i in range(1, n):
            for j in range(n):
                left = dp[i-1][j-1] if j > 0 else float('inf')
                up = dp[i-1][j]
                right = dp[i-1][j+1] if j < n-1 else float('inf')
                dp[i][j] += min(left, up, right)
        
    
        return min(dp[-1])
    



        