# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        copy = 0
        paste = 1
        ans = 0

        while paste != n:

            if n % paste == 0:
                copy = paste
                ans += 1

            paste += copy
            ans += 1

        return ans