# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
      
        athletes = [(s, i) for i, s in enumerate(score)]
        
        
        athletes.sort(reverse=True, key=lambda x: x[0])
        
        result = [""] * n
        for rank, (_, i) in enumerate(athletes, start=1):
            if rank == 1:
                result[i] = "Gold Medal"
            elif rank == 2:
                result[i] = "Silver Medal"
            elif rank == 3:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank)
        
        return result
