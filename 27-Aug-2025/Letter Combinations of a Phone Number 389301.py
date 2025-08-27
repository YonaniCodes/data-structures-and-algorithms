# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []

        num_to_char_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        combinations = []

    
        def back(i):
            if i == len(digits):
                res.append("".join(combinations))
                return

        
            for char in num_to_char_map[digits[i]]:
                combinations.append(char)
                back(i + 1)
                combinations.pop() 

        back(0)
        return res
        