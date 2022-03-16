#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
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
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, 0, self.countNodes(root))

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def dfs(self, root: Optional[TreeNode], idx: int, total: int) -> bool:
        if not root:
            return True
        if idx >= total:
            return False
        return self.dfs(root.left, idx*2+1, total) and self.dfs(
            root.right, idx*2+2, total
        )

# @lc code=end

