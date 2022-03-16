/*
 * @lc app=leetcode id=24 lang=cpp
 *
 * [24] Swap Nodes in Pairs
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
  ListNode* swapPairs(ListNode* head) {
    ListNode dummy, *curr = &dummy;
    curr->next = head;

    while (curr->next and curr->next->next) {
      ListNode *a = curr->next, *b = curr->next->next, *n = b->next;
      curr->next = b;
      b->next = a;
      a->next = n;
      curr = a;
    }

    return dummy.next;
  }
};
// @lc code=end
