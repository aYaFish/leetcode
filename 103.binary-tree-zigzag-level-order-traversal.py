#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        queue = deque([root])
        from_left = True

        while queue:
            size = len(queue)
            level = []
            while size:
                curr = queue.popleft()
                level.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
                size -= 1
            if from_left:
                ans.append(level)
            else:
                ans.append(level[::-1])
            from_left = not from_left
        
        return ans
# @lc code=end

