# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        # Iterate through the rest of the array
        for num in nums[k:]:
            if num > min_heap[0]:  # Only push if current num is larger than heap min
                heapq.heappushpop(min_heap, num)

        # The root of the heap is the kth largest
        return min_heap[0]
