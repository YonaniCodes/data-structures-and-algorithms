# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, root.val)]
        total_sum = 0

        while stack:
            node, curr_number = stack.pop()

            # If it's a leaf, add the number to the total
            if not node.left and not node.right:
                total_sum += curr_number

            # Push right and left children to stack if they exist
            if node.right:
                stack.append((node.right, curr_number * 10 + node.right.val))
            if node.left:
                stack.append((node.left, curr_number * 10 + node.left.val))

        return total_sum

