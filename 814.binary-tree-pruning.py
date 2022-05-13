#
# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        def helper(root: Optional[TreeNode]) -> bool:
            if not root:
                return False
            
            left = helper(root.left)
            right = helper(root.right)
            mid = True if root.val == 1 else False

            if not left:
                root.left = None
            if not right:
                root.right = None
            
            return left or right or mid
        
        result = helper(root)
        if not result:
            return None
        return root


        
# @lc code=end

