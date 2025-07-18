# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        opCount = 0 
        myNext = nums[-1]
        for i in range(len(nums)-2, -1, -1): 
            
            curOp = nums[i]//myNext + 1 if nums[i]%myNext else nums[i]//myNext 
            opCount += curOp - 1 
            myNext = nums[i]//curOp

        return opCount