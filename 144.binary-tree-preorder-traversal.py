#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = deque()

        while root or stack:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.left
            
            root = stack[-1]
            stack.pop()
            root = root.right
        
        return ans

# @lc code=end

