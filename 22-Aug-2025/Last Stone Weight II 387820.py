# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for stone in stones:
            for w in range(target, stone - 1, -1):
                if dp[w - stone]:
                    dp[w] = True
        
        for w in range(target, -1, -1):
            if dp[w]:
                return total - 2 * w