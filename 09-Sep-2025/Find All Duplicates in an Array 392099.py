# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for num in nums:
            index = abs(num) - 1  
            
            if nums[index] < 0:
                res.append(abs(num))  
            else:
                nums[index] = -nums[index]  
        
        return res
