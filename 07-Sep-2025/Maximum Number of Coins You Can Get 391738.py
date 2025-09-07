# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution(object):
    def maxCoins(self,piles):
        piles.sort()
        n = len(piles) // 3
        res = 0
       
        for i in range(len(piles) - 2, n - 1, -2):
            res += piles[i]
        return res
