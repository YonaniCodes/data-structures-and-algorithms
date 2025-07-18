# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal=len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            #check if we can reach the goal
            if i+ nums[i]>= goal:
                goal=i

        
        return goal==0