# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Input: weights: List[int], days: int
        # Output: int

        # Dry run1:
        # weights = [1,2,3,4,5,6,7,8,9,10], days = 5
        # [1,2,3,4,5], [6,7], [8], [9], [10]

        # A. Binary search
        # Time: O(n * logm)
        # Space: O(1)
        # n: weights.length
        # m: max candidate capacity = (len(weights)//days + 1) * max(weights)

        def is_valid_capacity(capacity):
            day_required = 1
            curr_weights = 0
            for weight in weights:
                curr_weights += weight
                if curr_weights > capacity:
                    day_required+=1
                    curr_weights = weight
            return day_required<=days

        # find smallest valid capacity
        # FFFFFF[T]TTTTTTT
        left, right = max(weights), (len(weights)//days+1) * max(weights)
        while left < right:
            mid = left + (right-left)//2
            if is_valid_capacity(mid):
                right = mid
            else:
                left = mid + 1

        return left