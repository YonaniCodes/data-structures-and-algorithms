# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length= len(arr)

        max_val=-1

        for i in range(length-1, -1,-1):
            temp= arr[i]
            arr[i]= max_val
            max_val= max(temp, arr[i])

       
        return arr
        