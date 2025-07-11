# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        # Step 1: Count the frequency of each number
        freq_map = Counter(nums)  # O(n)
        # Example: Counter({1: 3, 2: 2, 3: 1})

        # Step 2: Create frequency buckets
        # Index = frequency; value = list of numbers with that freq
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            bucket[freq].append(num)

        # Step 3: Go from highest freq to lowest, collect top k elements
        result = []
        for freq in range(len(bucket) - 1, 0, -1):  # from max to 1
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result
