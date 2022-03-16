#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy
        curr = head

        while curr and curr.next:
            first_node = curr
            second_node = curr.next
            next_node = curr.next.next

            prev.next = second_node
            second_node.next = first_node
            first_node.next = next_node

            prev = first_node
            curr = next_node

        return dummy.next
        
# @lc code=end

