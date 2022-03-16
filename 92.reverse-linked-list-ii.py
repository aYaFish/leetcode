#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, Tuple


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(-1, head)
        prev = dummy
        count = 1
        
        while prev and count < left:
            count += 1
            prev = prev.next
        
        prev.next = self.doReverse(prev.next, right - count + 1)
        return dummy.next
        
        
    def doReverse(self, start: ListNode, count: int) -> ListNode:
        curr = start
        prev = None
        while curr and count:
            count -= 1
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        start.next = curr
        
        return prev


        
    
# @lc code=end

