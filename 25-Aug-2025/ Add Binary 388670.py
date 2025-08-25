# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        one= int(a, 2)
        two=int(b,2)
        return bin(one+two)[2:]