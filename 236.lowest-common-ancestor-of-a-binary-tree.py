#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        ans = None

        def dfs(node: "TreeNode") -> bool:
            nonlocal ans

            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)
            mid = node == p or node == q

            if left + right + mid > 1:
                ans = node

            return left or right or mid

        dfs(root)
        return ans


# @lc code=end
