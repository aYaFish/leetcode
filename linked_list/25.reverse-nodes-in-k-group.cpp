/*
 * @lc app=leetcode id=25 lang=cpp
 *
 * [25] Reverse Nodes in k-Group
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
  ListNode *reverseKGroup(ListNode *head, int k) {
    ListNode *tail = head;
    int count = 0;
    while (++count < k and tail) {
      tail = tail->next;
    }

    if (count != k or !tail) return head;

    ListNode *next = tail->next;
    helper(head, k);
    head->next = reverseKGroup(next, k);

    return tail;
  }

  void helper(ListNode *head, int k) {
    ListNode *prev = nullptr;
    for (int i = 0; i < k; ++i) {
      ListNode *next = head->next;
      head->next = prev;
      prev = head;
      head = next;
    }
  }
};
// @lc code=end
