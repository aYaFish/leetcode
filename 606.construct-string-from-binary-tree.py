#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def helper(root):
            if not root:
                return "()"
            
            left_str = helper(root.left)
            right_str = helper(root.right)

            if left_str == "()" and right_str == "()":
                return f"{root.val}"
            if left_str == "()":
                return f"{root.val}()({right_str})"
            if right_str == "()":
                return f"{root.val}({left_str})"
            return f"{root.val}({left_str})({right_str})"

        return helper(root)
        
# @lc code=end

