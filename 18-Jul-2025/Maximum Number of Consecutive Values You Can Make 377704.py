# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        opCount = 0 
        myNext = nums[-1]
        for i in range(len(nums)-2, -1, -1): 
            
            curOp = nums[i]//myNext + 1 if nums[i]%myNext else nums[i]//myNext 
            opCount += curOp - 1 
            myNext = nums[i]//curOp

        return opCount