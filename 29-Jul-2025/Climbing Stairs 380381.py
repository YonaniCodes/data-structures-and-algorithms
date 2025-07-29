# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memory = {}
        def dp (num,memo):
            if num == 1 or num == 0:
                return 1
            if num not in memo:
               memo[num] = dp(num - 1, memo) + dp(num - 2, memo)
            return memo[num]
        return dp(n,memory)