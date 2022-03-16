/*
 * @lc app=leetcode id=23 lang=cpp
 *
 * [23] Merge k Sorted Lists
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
  ListNode *mergeKLists(vector<ListNode *> &lists) {
    auto comp = [](ListNode *a, ListNode *b) { return a->val > b->val; };

    priority_queue<ListNode *, vector<ListNode *>, decltype(comp)> pq(comp);
    for (auto list : lists) {
      if (list) pq.push(list);
    }

    ListNode dummy, *curr = &dummy;
    while (not pq.empty()) {
      curr->next = pq.top();
      pq.pop();

      curr = curr->next;
      if (curr and curr->next) {
        pq.push(curr->next);
      }
    }

    return dummy.next;
  }
};
// @lc code=end
