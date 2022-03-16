/*
 * @lc app=leetcode id=147 lang=cpp
 *
 * [147] Insertion Sort List
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
  ListNode* insertionSortList(ListNode* head) {
    ListNode dummy, *sorted = &dummy;

    while (head) {
      ListNode* next = head->next;
      sorted = &dummy;
      while (sorted->next and sorted->next->val < head->val) {
        sorted = sorted->next;
      }
      head->next = sorted->next;
      sorted->next = head;
      head = next;
    }

    return dummy.next;
  }
};
// @lc code=end
