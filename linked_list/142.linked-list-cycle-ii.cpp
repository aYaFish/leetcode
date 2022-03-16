/*
 * @lc app=leetcode id=142 lang=cpp
 *
 * [142] Linked List Cycle II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
 public:
  ListNode *detectCycle(ListNode *head) {
    if (!head) return nullptr;

    ListNode *slow = head, *fast = head->next;
    while (fast and fast->next) {
      if (slow == fast) break;
      slow = slow->next;
      fast = fast->next->next;
    }

    if (slow != fast) return nullptr;
    slow = head;
    while (slow != fast->next) {
      slow = slow->next;
      fast = fast->next;
    }

    return slow;
  }
};
// @lc code=end
