# Problem: Search in a BST - https://leetcode.com/problems/search-in-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node=root
        # print(node)
        while node and node.left and node.right:
            if node.val > val:
                node= node.left
            elif node.val< val:
               node= node.right
            else: 
                return node        