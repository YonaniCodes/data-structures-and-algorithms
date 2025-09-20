# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
    
        n = len(nums)
        res = 0
        for i in range(n):
            curr= 1
            for j in range(i,n):
                curr = math.lcm(curr,nums[j])
                if curr>k:
                    break

                if curr == k:
                    res+=1
        return res

