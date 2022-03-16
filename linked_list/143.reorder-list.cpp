/*
 * @lc app=leetcode id=143 lang=cpp
 *
 * [143] Reorder List
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
  void reorderList(ListNode *head) {
    ListNode *slow = head, *fast = head->next;
    while (fast and fast->next) {
      slow = slow->next;
      fast = fast->next->next;
    }

    ListNode *reverse = reverseList(slow->next);
    slow->next = nullptr;

    ListNode *origin = head;

    while (origin and reverse) {
      ListNode *no = origin->next, *nr = reverse->next;
      origin->next = reverse;
      reverse->next = no;
      origin = no;
      reverse = nr;
    }
  }

  ListNode *reverseList(ListNode *head) {
    ListNode *prev = nullptr;
    while (head) {
      ListNode *next = head->next;
      head->next = prev;
      prev = head;
      head = next;
    }

    return prev;
  }
};
// @lc code=end
