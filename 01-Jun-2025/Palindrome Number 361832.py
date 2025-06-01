# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        reversed_num = 0
        temp_x = x

        while temp_x != 0:
            current = temp_x % 10
            reversed_num = reversed_num * 10 + current
            temp_x //= 10  # Use integer division

        return reversed_num == x
