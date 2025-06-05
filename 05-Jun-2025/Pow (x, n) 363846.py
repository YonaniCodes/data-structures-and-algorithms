# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # define the base case
        if n==0:
            return 1
        #call the function recursively
        if n<0:
            return 1/self.myPow(x,-n)
        
        return x*self.myPow(x,n-1)
        