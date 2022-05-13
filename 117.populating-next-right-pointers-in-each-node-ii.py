#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        def process(node: "Node") -> None:
            nonlocal left_most, prev
            if not node:
                return
            if prev:
                prev.next = node
            else:
                left_most = node
            prev = node

        left_most = root
        while left_most:
            curr = left_most
            left_most, prev = None, None
            while curr:
                process(curr.left)
                process(curr.right)
                curr = curr.next

        return root


# @lc code=end
