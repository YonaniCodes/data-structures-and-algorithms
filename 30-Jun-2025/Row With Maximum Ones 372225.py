# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = (-1, 0)  # (row_index, number_of_ones)

        for index, row in enumerate(mat):
            current_count = row.count(1)  # cleaner way to count 1s
            if current_count > max_ones[1]:
                max_ones = (index, current_count)

        return list(max_ones)
