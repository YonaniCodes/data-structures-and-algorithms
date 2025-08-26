# Problem: Reducing Dishes - https://leetcode.com/problems/reducing-dishes/

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        total, res = 0, 0
        
        for x in satisfaction:
            total+=x
            if total > 0:
                res += total
            else: break
        
        return res