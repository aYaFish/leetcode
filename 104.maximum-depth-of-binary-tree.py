#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return max(dfs(root.left), dfs(root.right)) + 1
        
        return dfs(root)
        
# @lc code=end

