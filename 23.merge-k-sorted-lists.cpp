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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto cmp = [](ListNode* a, ListNode* b) {
            return a->val > b->val;
        };
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> pq(cmp);
        for(auto* l : lists) {
            if(l != nullptr) {
                pq.push(l);
            }
        }

        ListNode dummy, *tail = &dummy;
        while(!pq.empty()) {
            auto* curr = pq.top();
            pq.pop();

            tail->next = curr;
            tail = curr;
            if(curr->next) {
                pq.push(curr->next);
            }
        }
        return dummy.next;
    }
};
// @lc code=end

