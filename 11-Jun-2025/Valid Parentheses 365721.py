# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]
        bracket_map={"(":")","[":"]","{":"}"}

        for i in range( len(s)):
            if s[i] in bracket_map.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False

                last_opening= stack.pop()

                if bracket_map[last_opening] != s[i]:
                    return False
        return not stack

        