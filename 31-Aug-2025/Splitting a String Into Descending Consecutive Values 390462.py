# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(i,prev):
            if i == len(s):
                return True

            for j in range(i,len(s)):
                val = int(s[i:j+1])

                if val == prev - 1 and backtrack(j+1,val):
                    return True

        for i in range(len(s)-1):
            val = int(s[:i + 1])
            if backtrack(i+1, val):
                return True
        return False



