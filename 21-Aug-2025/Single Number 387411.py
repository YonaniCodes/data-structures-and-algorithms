# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        one= nums[0]
        for index in range(1, len(nums)):
            one= one^ nums[index]
        return one
        