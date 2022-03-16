/*
 * @lc app=leetcode id=148 lang=cpp
 *
 * [148] Sort List
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
  ListNode *sortList(ListNode *head) {
    if (!head or !head->next) return head;
    ListNode *slow = head, *fast = head->next;
    while (fast and fast->next) {
      slow = slow->next;
      fast = fast->next->next;
    }

    ListNode *right = sortList(slow->next);
    slow->next = nullptr;
    ListNode *left = sortList(head);

    return combine(left, right);
  }

  ListNode *combine(ListNode *left, ListNode *right) {
    ListNode dummy, *curr = &dummy;
    while (left and right) {
      if (left->val < right->val) {
        curr->next = left;
        left = left->next;
      } else {
        curr->next = right;
        right = right->next;
      }
      curr = curr->next;
    }
    if (left) {
      curr->next = left;
    } else {
      curr->next = right;
    }
    return dummy.next;
  }
};
// @lc code=end
