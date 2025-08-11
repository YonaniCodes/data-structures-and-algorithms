# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def dp(num):
            if num == 0:
                return 0
            if num == 1 or num == 2:
                return 1
            if num in memo:
                return memo[num]
            memo[num] = dp(num - 1) + dp(num - 2) + dp(num - 3)
            return memo[num]

        return dp(n)

        