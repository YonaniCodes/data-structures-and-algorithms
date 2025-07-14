# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

import heapq
from typing import List

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Max heap by storing negative numbers
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            reduced = ceil(largest/2)  
            heapq.heappush(max_heap, -reduced)

        return -sum(max_heap)
