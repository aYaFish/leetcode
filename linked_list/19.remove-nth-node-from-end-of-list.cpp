/*
 * @lc app=leetcode id=19 lang=cpp
 *
 * [19] Remove Nth Node From End of List
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
  ListNode *removeNthFromEnd(ListNode *head, int n) {
    ListNode dummy, *curr = &dummy;
    dummy.next = head;

    while (n > 0 and curr) {
      curr = curr->next;
      --n;
    }

    ListNode *prev = &dummy;
    while (curr and curr->next) {
      prev = prev->next;
      curr = curr->next;
    }

    prev->next = prev->next->next;
    return dummy.next;
  }
};
// @lc code=end
