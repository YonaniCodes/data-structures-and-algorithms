# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution(object):
    def findRightInterval(self,intervals):
        starts = sorted((start, i) for i, (start, _) in enumerate(intervals))
        result = []
        
        for _, end in intervals:
            idx = bisect_left(starts, (end,))
            result.append(starts[idx][1] if idx < len(starts) else -1)
        
        return result