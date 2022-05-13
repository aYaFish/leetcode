# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0
        if not root:
            return count

        def dfs(node: Optional[TreeNode]) -> bool:
            nonlocal count

            if not node.left and not node.right:
                count += 1
                return True

            left_result = True
            if node.left:
                left_result = dfs(node.left) and node.val == node.left.val

            right_result = True
            if node.right:
                right_result = dfs(node.right) and node.val == node.right.val

            if left_result and right_result:
                count += 1
                return True

            return False

        dfs(root)
        return count
