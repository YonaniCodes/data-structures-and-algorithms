# Problem: Prime Palindrome - https://leetcode.com/problems/prime-palindrome/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

 
        if n <= 2:
            return 2
        if n <= 11:
            for x in [2, 3, 5, 7, 11]:
                if x >= n:
                    return x

       
        for length in range(1, 6): 
            start = 10 ** (length - 1)
            end = 10 ** length
            for root in range(start, end):
                s = str(root)
                pal = int(s + s[-2::-1])   
                if pal >= n and is_prime(pal):
                    return pal

