# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(root,sumv,path):
            if not root:
                return
            sumv+=root.val
            path.append(root.val)
            if not root.left and not root.right and sumv == targetSum:
                res.append(path)
            dfs(root.left,sumv,path.copy())
            dfs(root.right,sumv,path.copy())
        
        dfs(root,0,[])
        return res