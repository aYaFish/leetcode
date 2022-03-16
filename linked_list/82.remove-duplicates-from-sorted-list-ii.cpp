/*
 * @lc app=leetcode id=82 lang=cpp
 *
 * [82] Remove Duplicates from Sorted List II
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
  ListNode* deleteDuplicates(ListNode* head) {
    ListNode dummy, *prev = &dummy, *curr = head;
    prev->next = curr;

    while (curr) {
      ListNode* node = curr;
      while (node and node->next and node->val == node->next->val) {
        node = node->next;
      }

      if (node == curr) {
        prev->next = node;
        prev = node;
      } else {
        prev->next = node->next;
      }
      curr = node->next;
    }

    return dummy.next;
  }
};
// @lc code=end
