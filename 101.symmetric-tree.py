#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(
            left_tree: Optional[TreeNode], right_tree: Optional[TreeNode]
        ) -> bool:
            if not left_tree and not right_tree:
                return True
            if not left_tree or not right_tree:
                return False

            if left_tree.val != right_tree.val:
                return False

            return dfs(left_tree.left, right_tree.right) and dfs(
                left_tree.right, right_tree.left
            )

        return dfs(root.left, root.right)


# @lc code=end
