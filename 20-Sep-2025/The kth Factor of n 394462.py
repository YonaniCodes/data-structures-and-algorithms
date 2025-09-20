# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
 
        factor = []
 
        for i in range(1,int((n**0.5)+1)):
            if n%i == 0:
                if i != n//i:
                    factor.append(i)
                    factor.append(n//i)
                else:
                    factor.append(i)

        factor.sort()
        n = len(factor)
 
        if k-1 > n-1:
            return -1
        else:
            return factor[k-1]
