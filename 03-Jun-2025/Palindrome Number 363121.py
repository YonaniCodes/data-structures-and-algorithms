# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #number is negative canot be palindrom
        if x<0:
            return False
        #reverse the number
        reversed_number=self.reverseNumber(x)

        #return true if the reversed ande actual number are equal
        return x== reversed_number
    def reverseNumber(self, num:int)-> int:
        revrsed_number=0

        while num >0:
            #get the last digit
            last_digit= num%10
            #add the digit to the end of the revrsed number
            revrsed_number= revrsed_number*10 + last_digit
            # remove the last digit form the number
            num= num//10
        return revrsed_number

        