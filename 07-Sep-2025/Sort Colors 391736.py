# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution(object):
   def sortColors(self,nums):
    count0 = count1 = count2 = 0
    for num in nums:
        if num == 0: count0 += 1
        elif num == 1: count1 += 1
        else: count2 += 1

    i = 0
    nums[:count0] = [0] * count0
    nums[count0:count0+count1] = [1] * count1
    nums[count0+count1:] = [2] * count2

        