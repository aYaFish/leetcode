#
# @lc app=leetcode id=298 lang=python3
#
# [298] Binary Tree Longest Consecutive Sequence
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, Tuple

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal result
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            length = 1
            if root.left and root.left.val == root.val + 1:
                length = max(length, left + 1)
            if root.right and root.right.val == root.val + 1:
                length = max(length, right + 1)
            
            result = max(result, length)
            return length
        
        dfs(root)
        return result

        
# @lc code=end

