# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    def __init__(self):
        # Initialize a dictionary to cache computed Fibonacci numbers
        self.memo = {}

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in (0, 1):
            return n
        
        if n in self.memo:
            return self.memo[n]
        
        # Recursively compute fib(n-1) and fib(n-2)
        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]
# /