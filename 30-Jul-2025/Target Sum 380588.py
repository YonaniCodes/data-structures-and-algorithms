# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        # Check if (total + target) is valid and even
        if (total + target) % 2 != 0 or total < abs(target):
            return 0
        
        subset_sum = (total + target) // 2
        
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # There is 1 way to make sum 0 — pick nothing
        
        for num in nums:
            for i in range(subset_sum, num - 1, -1):
                dp[i] += dp[i - num]
        
        return dp[subset_sum]
