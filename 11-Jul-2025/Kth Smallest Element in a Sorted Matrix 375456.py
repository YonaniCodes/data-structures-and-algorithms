# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        minHeap = []

        # Put the first element of each row into the heap
        for row in range(min(k, n)):  # Don't add more than k rows
            # (value, row, col)
            heapq.heappush(minHeap, (matrix[row][0], row, 0))

        # Pop k-1 elements
        for _ in range(k - 1):
            val, r, c = heapq.heappop(minHeap)

            # If there's a next column in the same row, push it
            if c + 1 < n:
                heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1))

        return heapq.heappop(minHeap)[0]
