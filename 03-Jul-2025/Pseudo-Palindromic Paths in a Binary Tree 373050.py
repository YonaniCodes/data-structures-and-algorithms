# Problem: Pseudo-Palindromic Paths in a Binary Tree - https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/?envType=daily-question&envId=2024-01-24

from collections import Counter
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, [])]  # Stack holds tuples of (node, current_path_list)
        count = 0

        def is_pseudo_palindromic(path):
            freq = Counter(path)
            odd_count = sum(1 for val in freq.values() if val % 2 != 0)
            return odd_count <= 1

        while stack:
            node, path = stack.pop()
            path = path + [node.val]  # create a new path for this node

            if not node.left and not node.right:  # leaf
                if is_pseudo_palindromic(path):
                    count += 1
            if node.right:
                stack.append((node.right, path))
            if node.left:
                stack.append((node.left, path))

        return count
