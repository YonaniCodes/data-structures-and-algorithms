# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or k == 0:
            return []

        minHeap = []
        visited = set()
        res = []

        # Push the first pair (smallest sum) into the heap
        heapq.heappush(minHeap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))

        while minHeap and len(res) < k:
            total, i, j = heapq.heappop(minHeap)
            res.append([nums1[i], nums2[j]])

            # Push the next element in nums1 (move down)
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(minHeap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            # Push the next element in nums2 (move right)
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

        return res
