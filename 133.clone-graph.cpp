/*
 * @lc app=leetcode id=133 lang=cpp
 *
 * [133] Clone Graph
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
 public:
  Node *cloneGraph(Node *node) {
    if (node == nullptr) {
      return node;
    }

    queue<Node *> que;
    unordered_map<Node *, Node *> hash;

    que.push(node);

    while (!que.empty()) {
      Node *curr = que.front();
      que.pop();

      Node *newNode = new Node(curr->val);
      hash[curr] = newNode;

      for (auto *neighbor : curr->neighbors) {
        if (hash.count(neighbor)) {
          continue;
        }
        que.push(neighbor);
      }
    }

    for (auto &it : hash) {
      for (auto *neighbor : it.first->neighbors) {
        it.second->neighbors.push_back(hash[neighbor]);
      }
    }

    return hash[node];
  }
};
// @lc code=end
