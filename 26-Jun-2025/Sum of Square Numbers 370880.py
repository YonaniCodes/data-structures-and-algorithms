# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max_val= int(math.sqrt(c))

        left=0
        right= max_val

        while left<=right:
            squred= left*left + right*right

            if squred==c:
                return True
            elif squred>c:
                right-=1
            elif squred<c:
                left+=1
        return False