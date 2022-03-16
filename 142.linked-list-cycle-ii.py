#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            if slow == fast.next:
                break
            slow = slow.next
            fast = fast.next.next
        else:
            return None
        
        fast = head
        while slow.next != fast:
            slow = slow.next
            fast = fast.next
        
        return fast



# @lc code=end

