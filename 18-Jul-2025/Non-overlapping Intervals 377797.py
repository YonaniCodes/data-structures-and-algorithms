# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort( key= lambda x: x[1])
        prev_end = intervals[0][1]  # Take the end of the first interval
        remove_count = 0
    
        # Start from the second interval
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            if start >= prev_end:
                # No overlap → update prev_end
                prev_end = end
            else:
                # Overlap → remove this interval
                remove_count += 1
                
        return remove_count
