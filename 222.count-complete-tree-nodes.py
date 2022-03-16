#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        height = 0
        left, right = root.left, root.right
        while right:
            height += 1
            left = left.left
            right = right.right
        if not left:
            return (2 << height) - 1
        # There's at least one subtree is full, so it returns directly and
        # continue to count the other side
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# @lc code=end

