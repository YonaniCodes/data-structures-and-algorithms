# Problem: Largest Odd Number in String - https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd_idx = float('inf')
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2:
                odd_idx = i
                break
        return num[:odd_idx+1] if odd_idx != float('inf') else ""