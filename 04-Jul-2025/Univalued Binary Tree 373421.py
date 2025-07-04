# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

from collections import deque
from typing import Optional

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
        # self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        target = root.val
        queue = deque([root])

        while queue:
            current = queue.popleft()

            if current.val != target:
                return False

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return True
 