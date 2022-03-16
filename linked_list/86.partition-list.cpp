/*
 * @lc app=leetcode id=86 lang=cpp
 *
 * [86] Partition List
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
  ListNode* partition(ListNode* head, int x) {
    ListNode first_head, *first_tail = &first_head;
    ListNode second_head, *second_tail = &second_head;

    while (head) {
      if (head->val < x) {
        first_tail->next = head;
        first_tail = head;
      } else {
        second_tail->next = head;
        second_tail = head;
      }
      head = head->next;
    }

    first_tail->next = second_head.next;
    second_tail->next = nullptr;

    return first_head.next;
  }
};
// @lc code=end
