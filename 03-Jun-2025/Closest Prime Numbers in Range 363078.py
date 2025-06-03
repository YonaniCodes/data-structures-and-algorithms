# Problem: Closest Prime Numbers in Range - https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        #  variable to store the difference between two consquetive
        difference= float("inf")

        nums=[-1,-1]
        perviouse_prime_number=-1
      

        for i in range(left,right+1):
            #check if the number is prime
            if self.isPrime(i):
                #check if there is a prime found before
                if perviouse_prime_number!=-1:
                    #check if the difference is small
                    if (i- perviouse_prime_number)< difference:
                        difference= i-perviouse_prime_number
                        nums=[perviouse_prime_number,i]

                perviouse_prime_number=i
                

        return nums
                    



    def isPrime(self, num):
        if num <= 1:
            return False  # 0 and 1 are not prime
        if num== 2:
            return True   # 2 is the only even prime number
        if num % 2 == 0:
            return False  # eliminate even numbers

        for i in range(3, int(num ** 0.5) + 1, 2):  # check only odd divisors
            if num % i == 0:
                return False
        return True



