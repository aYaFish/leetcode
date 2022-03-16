#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))
        
        dummy = ListNode()
        curr = dummy
        while min_heap:
            _, level, node = heapq.heappop(min_heap)
            curr.next = node
            if node.next:
                heapq.heappush(min_heap, (node.next.val, level, node.next))
            curr = curr.next
        
        return dummy.next
# @lc code=end

