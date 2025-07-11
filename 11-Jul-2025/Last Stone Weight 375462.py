# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        # Convert to a max heap by pushing negative values
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)  # largest
            second = -heapq.heappop(stones) # second largest

            if first != second:
                # Push the difference back into the heap
                heapq.heappush(stones, -(first - second))

        # Return the last stone or 0
        return -stones[0] if stones else 0
