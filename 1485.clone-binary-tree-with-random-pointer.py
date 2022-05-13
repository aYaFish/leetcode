#
# @lc app=leetcode id=1485 lang=python3
#
# [1485] Clone Binary Tree With Random Pointer
#

# @lc code=start
# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random


class Solution:
    def copyRandomBinaryTree(
        self, root: "Optional[Node]"
    ) -> "Optional[NodeCopy]":
        def copyNode(node: "Node") -> None:
            nonlocal h
            if not node:
                return

            new_node = NodeCopy(node.val)
            h[node] = new_node

            copyNode(node.left)
            copyNode(node.right)

        def copyEdge(node: "Node") -> None:
            nonlocal h
            if not node:
                return

            new_node = h[node]
            if node.left:
                new_node.left = h[node.left]
            if node.right:
                new_node.right = h[node.right]
            if node.random:
                new_node.random = h[node.random]

            copyEdge(node.left)
            copyEdge(node.right)

        h = {}
        copyNode(root)
        copyEdge(root)

        return h.get(root, None)


# @lc code=end
