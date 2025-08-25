# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []   # stores all subsets (final result)

        def dfs(start_index: int, current_subset: List[int]):
       
            subsets.append(current_subset[:])

  
            for i in range(start_index, len(nums)):
        
                current_subset.append(nums[i])
 
                dfs(i + 1, current_subset)
 
                current_subset.pop()

 
        dfs(0, [])

        return subsets
