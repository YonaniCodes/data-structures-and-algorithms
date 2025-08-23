# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        def backtrack(start, path):
            if start == n and len(path) >= 3:
                return True
            for i in range(start + 1, n + 1):
                curr = num[start:i]
                if len(curr) > 1 and curr[0] == '0':
                    break
                curr_num = int(curr)
                if len(path) >= 2:
                    if path[-1] + path[-2] != curr_num:
                        continue
                if backtrack(i, path + [curr_num]):
                    return True
            return False
        return backtrack(0, [])