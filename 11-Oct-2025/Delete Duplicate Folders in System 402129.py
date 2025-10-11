# Problem: Delete Duplicate Folders in System - https://leetcode.com/problems/delete-duplicate-folders-in-system/description/

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # so this might be the most complex solution to come up with
        # I use editorial and it took me hours to understand it 
        # I am not even sure if I understood it :(
        

        # create a dp array ,and fill it up with the minimum left overs we can get
        n = len(s)
        _dict = set(dictionary)
        dp = [0] * (n+1)

        # iterate from the last
        for pos in range(n-1,-1,-1):
            dp[pos] = 1+dp[pos+1]  # this considers that all the characters after this positon is a leftover
            for end in range(pos,n): # this is an efficient way of finding substrings
                sub = s[pos:end+1]

                if sub in _dict:
                    dp[pos] = min(dp[pos],dp[end+1])  #this line is a bit complex

        return dp[0]

