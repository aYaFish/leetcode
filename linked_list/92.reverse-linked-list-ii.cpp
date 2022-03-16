/*
 * @lc app=leetcode id=92 lang=cpp
 *
 * [92] Reverse Linked List II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
 public:
  ListNode *reverseBetween(ListNode *head, int left, int right) {
    ListNode dummy, *curr = &dummy;
    curr->next = head;

    int i = 1;
    while (i++ < left and curr) {
      curr = curr->next;
    }
    ListNode *prev_left = curr;

    i = left - 1;
    while (i++ <= right and curr) {
      curr = curr->next;
    }
    ListNode *after_right = curr;

    prev_left->next = helper(prev_left->next, after_right);

    return dummy.next;
  }

  ListNode *helper(ListNode *start, ListNode *end) {
    ListNode *prev = end;
    while (start != end) {
      ListNode *next = start->next;
      start->next = prev;
      prev = start;
      start = next;
    }

    return prev;
  }
};
// @lc code=end
