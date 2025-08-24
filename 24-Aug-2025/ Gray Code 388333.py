# Problem:  Gray Code - https://leetcode.com/problems/gray-code/description/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        output= []
        for i in range(1 << n):
            output.append(i ^ (i >> 1))
        return output