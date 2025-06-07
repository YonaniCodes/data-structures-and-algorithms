# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(start: int, combination: List[int]):
            if len(combination) == k:
                ans.append(combination[:])
                return

            for num in range(start, n + 1):
                combination.append(num)
                backtrack(num + 1, combination)
                combination.pop()

        backtrack(1, [])
        return ans
