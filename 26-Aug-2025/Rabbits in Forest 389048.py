# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        groups = defaultdict(int)
        count = 0
        for value in answers: 
            if not value:
                count += 1
                continue
            groups[value+1] += 1
            if groups[value+1] == value + 1:
                count += value+1
                del groups[value + 1]
            
        for key in groups:
            count += key
        return count