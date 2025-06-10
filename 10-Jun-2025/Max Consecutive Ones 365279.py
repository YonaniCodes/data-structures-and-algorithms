# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count=0
        current_max=0

        for num in nums:
            if num==1:
                current_max+=1
                max_count= max(current_max, max_count)                
            elif num==0:
                current_max=0
 
        return max_count
        left=0
        max_len=0

        # for right in range(len(nums)):
        #     if nums[right]==0:
        #         #move left 0 is found
        #         left=right+1
        #     else:
        #         max_len=max(max_len,right-left+1)
        # return max_len





        