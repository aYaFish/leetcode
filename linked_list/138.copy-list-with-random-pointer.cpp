/*
 * @lc app=leetcode id=138 lang=cpp
 *
 * [138] Copy List with Random Pointer
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
 public:
  Node* copyRandomList(Node* head) {
    // Duplicate
    Node* curr = head;
    while (curr) {
      Node* node = new Node(curr->val);
      node->next = curr->next;
      curr->next = node;
      curr = node->next;
    }

    // Copy random
    curr = head;
    while (curr) {
      if (curr->random) {
        curr->next->random = curr->random->next;
      }
      curr = curr->next->next;
    }

    // Separate
    curr = head;
    Node dummy(0), *tail = &dummy;
    while (curr) {
      tail->next = curr->next;
      tail = tail->next;

      curr->next = curr->next->next;
      curr = curr->next;
    }

    return dummy.next;
  }
};
// @lc code=end
