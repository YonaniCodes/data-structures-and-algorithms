# Problem: Jump Game - https://leetcode.com/problems/jump-game/

 
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by costA - costB
        costs.sort(key=lambda x: x[0] - x[1])
        
        n = len(costs) // 2
        total = 0
        
        # First half -> city A
        for i in range(n):
            total += costs[i][0]
        
        # Second half -> city B
        for i in range(n, 2 * n):
            total += costs[i][1]
        
        return total
