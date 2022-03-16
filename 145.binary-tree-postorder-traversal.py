#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        prev = None
        ans = []
        stack = deque()

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack[-1]
            if root.right and root.right != prev:
                root = root.right
                continue
            ans.append(root.val)
            prev = root
            root = None
            stack.pop()
        
        return ans
            


# @lc code=end

