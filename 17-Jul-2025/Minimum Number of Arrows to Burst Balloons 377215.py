# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Step 1: Sort balloons by their ending point
        points.sort(key=lambda x: x[1])

        arrows = 1  # At least one arrow is needed
        prev_end = points[0][1]  # Place the first arrow at the end of the first balloon

        for start, end in points[1:]:
            if start > prev_end:
                # Need a new arrow
                arrows += 1
                prev_end = end  # Update position of the new arrow

        return arrows
