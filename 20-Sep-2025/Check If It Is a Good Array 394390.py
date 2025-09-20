# Problem: Check If It Is a Good Array - https://leetcode.com/problems/check-if-it-is-a-good-array/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        res=num[0]
        for num in nums:
            res=gcd(res,num)
        return res==1