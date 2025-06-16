# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # score[i] = # of incoming trusts  − # of times i trusts others
        score = [0] * (n + 1)
        
        # Accumulate trust scores
        for a, b in trust:
            score[a] -= 1
            score[b] += 1
        
        # Look for the one with score == n-1
        for person in range(1, n + 1):
            if score[person] == n - 1:
                return person
        
        return -1
