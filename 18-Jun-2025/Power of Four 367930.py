# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
         # basecases
        if n==1:
            return True
        if n<1:
            return False 
        if n%4!=0:
            return False
        return self.isPowerOfFour(n/4)


