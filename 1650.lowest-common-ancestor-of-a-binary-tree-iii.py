#
# @lc app=leetcode id=1650 lang=python3
#
# [1650] Lowest Common Ancestor of a Binary Tree III
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        p_path, q_path = deque(), deque()

        def back_track(node: "Node", path: "deque") -> None:
            while node:
                path.appendleft(node)
                node = node.parent

        back_track(p, p_path)
        back_track(q, q_path)

        ans = None
        while p_path and q_path and p_path[0] == q_path[0]:
            ans = p_path.popleft()
            q_path.popleft()

        return ans


# @lc code=end
