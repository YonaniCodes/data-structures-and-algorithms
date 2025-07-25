# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
    
        right_max = 0
        left_max = 0
        left_max_arr = []
        right_max_arr = [0]*len(height)
        i=0
        j=len(height)-1
        total = 0
        while j>-1 and i<len(height):
            left_max_arr.append(left_max)
            left_max = max(left_max, height[i])
            right_max_arr[j] = right_max
            right_max = max(right_max, height[j])
            j-=1
            i+=1
        for i in range(len(height)):
            num = min(left_max_arr[i], right_max_arr[i]) - height[i]
            total += 0 if num < 0 else num
            
        return total