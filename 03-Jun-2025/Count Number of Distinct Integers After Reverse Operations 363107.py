# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct = set(nums)

        for num in nums:
            reversed_num = self.reverse(num)
            distinct.add(reversed_num)
        
        return len(distinct)

    def reverse(self, num):
        reversed_num = 0
        while num > 0:
            last_digit = num % 10
            reversed_num = reversed_num * 10 + last_digit
            num = num // 10
        return reversed_num
# 