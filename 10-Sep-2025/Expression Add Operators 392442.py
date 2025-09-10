# Problem: Expression Add Operators - https://leetcode.com/problems/expression-add-operators/description/

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        def back(pre, idx):
            if idx == len(num):
                if eval(pre) == target:
                    ans.append(pre)
                return
            for op in ['+', '-', '*', '']:
                if op == '' and pre[-1] == '0' and (len(pre) == 1 or pre[-2] in '+-*'):
                    continue
                npre = pre + op + num[idx]
                back(npre, idx + 1)
        back(num[0], 1)
        return ans