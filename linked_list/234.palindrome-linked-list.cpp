/*
 * @lc app=leetcode id=234 lang=cpp
 *
 * [234] Palindrome Linked List
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
  bool isPalindrome(ListNode *head) {
    if (!head or !head->next) return true;
    ListNode *slow = head, *fast = head->next;
    while (fast and fast->next) {
      slow = slow->next;
      fast = fast->next->next;
    }
    ListNode *tail = reverseList(slow->next);
    slow->next = nullptr;

    while (head and tail and head->val == tail->val) {
      head = head->next;
      tail = tail->next;
    }

    return tail == nullptr;
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
