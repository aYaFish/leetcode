/*
 * @lc app=leetcode id=382 lang=cpp
 *
 * [382] Linked List Random Node
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
  /** @param head The linked list's head.
      Note that the head is guaranteed to be not null, so it contains at least
     one node. */
  Solution(ListNode *head) { this->head = head; }

  /** Returns a random node's value. */
  int getRandom() {
    ListNode *curr = head;
    int ans = 0, len = 0;
    while (curr) {
      ++len;
      if (rand() % len + 1 == 1) {
        ans = curr->val;
      }
      curr = curr->next;
    }
    return ans;
  }

 private:
  ListNode *head;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
// @lc code=end