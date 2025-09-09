# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Initialize a boolean array, True means "prime"
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False  # 0 and 1 are not prime
        
        # Sieve of Eratosthenes
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        
        # Count primes
        return sum(isPrime)
