/*
 * @lc app=leetcode id=725 lang=cpp
 *
 * [725] Split Linked List in Parts
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
  vector<ListNode *> splitListToParts(ListNode *head, int k) {
    int len = getLength(head);
    int s = len / k, a = len % k;

    ListNode *curr = head;
    vector<ListNode *> ans(k);

    for (int i = 0; i < k; ++i) {
      ans[i] = curr;
      ListNode *prev = nullptr;
      int r = s + (a-- > 0 ? 1 : 0);
      while (r-- > 0) {
        prev = curr;
        curr = curr->next;
      }

      if (prev) {
        prev->next = nullptr;
      }
    }

    return ans;
  }

  int getLength(ListNode *head) {
    int len = 0;
    while (head) {
      ++len;
      head = head->next;
    }
    return len;
  }
};
// @lc code=end
