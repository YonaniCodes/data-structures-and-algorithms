# Problem: Pseudo-Palindromic Paths in a Binary Tree - https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/?envType=daily-question&envId=2024-01-24

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path=0):
            if not node:
                return 0

            # Toggle the bit for node.val
            path ^= 1 << node.val

            if not node.left and not node.right:
                # Check if path has at most one odd count
                return 1 if path & (path - 1) == 0 else 0

            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root)
