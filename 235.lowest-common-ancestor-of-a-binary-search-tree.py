#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
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
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)

        while root:
            if p.val <= root.val <= q.val:
                ans = root
                break
            if p.val > root.val:
                root = root.right
            else:
                root = root.left

        return ans


# @lc code=end
