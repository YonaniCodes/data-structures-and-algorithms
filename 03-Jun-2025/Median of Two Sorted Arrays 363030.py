# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        merged = []

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        if i < m:
            merged.extend(nums1[i:])
        if j < n:
            merged.extend(nums2[j:])

        total_len = m + n
        if total_len % 2 == 1:
            return float(merged[total_len // 2])
        else:
            mid = total_len // 2
            return (merged[mid - 1] + merged[mid]) / 2.0
