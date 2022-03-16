/*
 * @lc app=leetcode id=160 lang=cpp
 *
 * [160] Intersection of Two Linked Lists
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
  ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    if (!headA or !headB) return nullptr;
    int lenA = getLength(headA), lenB = getLength(headB);
    if (lenA < lenB) {
      swap(headA, headB);
      swap(lenA, lenB);
    }
    while (lenA-- > lenB) {
      headA = headA->next;
    }

    while (headA != headB) {
      headA = headA->next;
      headB = headB->next;
    }

    return headA;
  }

  int getLength(ListNode *head) {
    if (!head) return 0;
    int length = 0;
    while (head) {
      ++length;
      head = head->next;
    }
    return length;
  }
};
// @lc code=end
