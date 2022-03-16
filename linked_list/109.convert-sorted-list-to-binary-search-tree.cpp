/*
 * @lc app=leetcode id=109 lang=cpp
 *
 * [109] Convert Sorted List to Binary Search Tree
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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
 public:
  TreeNode* sortedListToBST(ListNode* head) {
    // if(!head) return nullptr;
    ListNode dummy, *slow = &dummy, *fast = head;
    slow->next = head;  // !!Don't forget to connect dummy to head

    while (fast and fast->next) {
      slow = slow->next;
      fast = fast->next->next;
    }

    if (!slow->next) return nullptr;
    TreeNode* root = new TreeNode(slow->next->val);

    root->right = sortedListToBST(slow->next->next);
    if (slow->next == head) {
      root->left = nullptr;
    } else {
      slow->next = nullptr;
      root->left = sortedListToBST(head);
    }

    return root;
  }
};
// @lc code=end
