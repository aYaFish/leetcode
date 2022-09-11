#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
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
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return None

        left_most = root
        while left_most:
            curr = left_most
            while curr and curr.left:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left

                curr = curr.next
            left_most = left_most.left

        return root


# @lc code=end
