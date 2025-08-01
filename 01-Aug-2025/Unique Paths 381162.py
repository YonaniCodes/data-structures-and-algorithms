# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #the last row when the loop starts executing
        row=[1]* n
        for i in range(m-1):
            newrow=[1]*n
            for j in range(n-2,-1,-1):
                newrow[j]= newrow[j+1]+ row[j]
            row=newrow

        return row[0]
