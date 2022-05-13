#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(
        self, root: Optional[TreeNode], targetSum: int
    ) -> List[List[int]]:
        ret = []
        curr = []

        def dfs(root: Optional[TreeNode], remaining: int) -> None:
            nonlocal ret, curr
            if not root:
                return

            curr.append(root.val)
            if not root.right and not root.left and remaining == root.val:
                ret.append(curr[:])
                curr.pop()
                return

            dfs(root.left, remaining - root.val)
            dfs(root.right, remaining - root.val)

            curr.pop()

        dfs(root, targetSum)
        return ret


# @lc code=end
