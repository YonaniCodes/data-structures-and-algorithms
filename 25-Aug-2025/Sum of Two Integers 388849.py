# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        while b != 0:
            sum_ = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK
            a, b = sum_, carry
        return a if a <= 0x7FFFFFFF else ~(a ^ MASK)