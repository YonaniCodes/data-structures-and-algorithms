# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        n = len(nums)
        _set = set()
        for i in range(n):
            divisor = 2
            x = nums[i]
            while x!=1:
                if x%divisor == 0:
                    _set.add(divisor)
                    
                    x//=divisor
                else:
                   
                    divisor+=1
    
        return len(_set)
