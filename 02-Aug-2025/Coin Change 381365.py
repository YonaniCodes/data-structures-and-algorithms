# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] *(amount + 1)
        dp[0]=0

        for i in range(amount + 1):
            if dp[i]!=-1:
                for coin in coins:
                    temp = i + coin
                    if temp <=amount:
                        if dp[temp]==-1 or dp[temp]>dp[i]+1:
                            dp[temp]=dp[i]+1
        return dp[amount]





        
