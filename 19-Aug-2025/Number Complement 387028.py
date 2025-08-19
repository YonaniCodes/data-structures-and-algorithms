# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)
        print(binary)
        complmet=""
        for index in range(2,len(binary)):
            # print(~(binary[index]), binary[index])
            if binary[index]=="1":
                complmet+="0"
            else:
                complmet+="1"


        return int(complmet,2)
        