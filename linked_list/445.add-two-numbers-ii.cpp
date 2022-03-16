/*
 * @lc app=leetcode id=445 lang=cpp
 *
 * [445] Add Two Numbers II
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
    l1 = reverseList(l1);
    l2 = reverseList(l2);

    ListNode *prev = nullptr;
    int carry = 0;

    while (l1 or l2) {
      int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
      carry = sum / 10;

      ListNode *curr = new ListNode(sum % 10);
      curr->next = prev;
      prev = curr;

      l1 = l1 ? l1->next : l1;
      l2 = l2 ? l2->next : l2;
    }

    if (carry) {
      ListNode *curr = new ListNode(carry);
      curr->next = prev;
      prev = curr;
    }

    return prev;
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
