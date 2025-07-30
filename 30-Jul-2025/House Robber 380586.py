# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0  # prev1 = dp[i-1], prev2 = dp[i-2]
        for num in nums:
            curr = max(prev1, num + prev2)
            prev2 = prev1
            prev1 = curr
        return prev1
        