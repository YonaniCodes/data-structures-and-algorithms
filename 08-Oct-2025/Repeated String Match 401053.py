# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        repeat = math.ceil(m / n)
        repeated_a = a * repeat
        if b in repeated_a:
            return repeat
        if b in repeated_a + a:
            return repeat + 1
        return -1