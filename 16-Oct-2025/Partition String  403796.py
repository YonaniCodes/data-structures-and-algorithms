# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        n  = len(s)
        ans = []
        _set = set()

        prev = 0
        for i in range(n):
            l = s[prev:i+1]
            if l not in _set:
                _set.add(l)
                ans.append(l)
                prev = i+1
            # else:
            #     prev = i
        return ans


        