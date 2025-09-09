# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

import math

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        return math.gcd(smallest, largest)