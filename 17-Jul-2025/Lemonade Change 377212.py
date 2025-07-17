# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0   # count of $5 bills
        ten = 0    # count of $10 bills

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                # Prefer to give one $10 and one $5 if possible
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

