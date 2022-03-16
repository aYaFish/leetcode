/*
 * @lc app=leetcode id=2 lang=cpp
 *
 * [2] Add Two Numbers
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
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    ListNode dummy, *curr = &dummy;
    int carry = 0;

    while (l1 or l2 or carry) {
      int val = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
      curr->next = new ListNode(val % 10);
      carry = val / 10;

      curr = curr->next;
      l1 = l1 ? l1->next : l1;
      l2 = l2 ? l2->next : l2;
    }

    return dummy.next;
  }
};
// @lc code=end
