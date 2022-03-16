/*
 * @lc app=leetcode id=328 lang=cpp
 *
 * [328] Odd Even Linked List
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
  ListNode* oddEvenList(ListNode* head) {
    if (!head or !head->next) return head;
    ListNode oddDummy, evenDummy;
    ListNode *oddTail = &oddDummy, *evenTail = &evenDummy;

    while (head) {
      oddTail->next = head;
      oddTail = oddTail->next;

      if (head->next) {
        evenTail->next = head->next;
        evenTail = evenTail->next;
        head = evenTail->next;
      } else {
        head = head->next;
      }
    }

    oddTail->next = evenDummy.next;
    evenTail->next = nullptr;

    return oddDummy.next;
  }
};
// @lc code=end
