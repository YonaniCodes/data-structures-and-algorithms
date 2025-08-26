# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
    
        total = 0     
        tank = 0       
        start = 0

        for i in range(n ):
            gain = gas[i] - cost[i]
            total += gain
            tank += gain

            if tank < 0:     
                start = i + 1
                tank = 0

        return start if total >= 0 else -1
