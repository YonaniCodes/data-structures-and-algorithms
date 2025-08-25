# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #first xor the two number
        #difference in bit means xor is one
        #count the bits which are one

        xor_value = x ^ y
        return bin(xor_value).count('1')
        