# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #avariable to hold the answer
        ans=[]

        #the trik is elimanting the numebr repeated nums 
        #if they'e repeated twice then xor will make the result zeor
        # vlaue= nums[0]
        # for i  in range(1,len(nums)):
        #     value=nums[i]^ vlaue
        # print(value)

        count= Counter(nums)

        return     [ key  for key, vlaue in count.values() if vlaue==1] 
 