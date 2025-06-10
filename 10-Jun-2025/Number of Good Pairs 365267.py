# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_count_map=Counter(nums)
        
        return sum( count*(count-1)//2 for count in  num_count_map.values())

        
