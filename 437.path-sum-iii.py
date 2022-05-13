#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        count = 0

        def dfs(node: Optional[TreeNode], prefix_sum: int) -> None:
            nonlocal count, hashmap
            if not node:
                return

            prefix_sum += node.val
            count += hashmap[prefix_sum - targetSum]

            # update hashmap after adjusting count
            hashmap[prefix_sum] += 1

            dfs(node.left, prefix_sum)
            dfs(node.right, prefix_sum)

            hashmap[prefix_sum] -= 1
            prefix_sum -= node.val

        dfs(root, 0)
        return count


# @lc code=end
