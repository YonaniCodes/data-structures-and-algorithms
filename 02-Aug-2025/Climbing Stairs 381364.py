# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
  def climbStairs(self,n:int)->int:
    one, two=1,1
    for _ in range(n-1):
      temp=one
      one= two+two
      two=temp