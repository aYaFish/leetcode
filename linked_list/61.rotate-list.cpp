/*
 * @lc app=leetcode id=61 lang=cpp
 *
 * [61] Rotate List
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
  ListNode* rotateRight(ListNode* head, int k) {
    if (!head or !k) return head;

    int len = 1;
    ListNode* tail = head;
    while (tail and tail->next) {
      tail = tail->next;
      ++len;
    }

    k = k % len;
    int m = len - k;
    ListNode* curr = head;
    while (m-- > 1) {
      curr = curr->next;
    }

    tail->next = head;
    head = curr->next;
    curr->next = nullptr;

    return head;
  }
};
// @lc code=end
