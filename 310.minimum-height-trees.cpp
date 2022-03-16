/*
 * @lc app=leetcode id=310 lang=cpp
 *
 * [310] Minimum Height Trees
 */

// @lc code=start
class Solution {
 public:
  vector<int> findMinHeightTrees(int n, vector<vector<int>> &edges) {
    if (n == 1) return {0};

    unordered_map<int, unordered_set<int>> adj;
    for (auto &edge : edges) {
      adj[edge[0]].insert(edge[1]);
      adj[edge[1]].insert(edge[0]);
    }
    vector<int> leaves;
    for (auto &item : adj) {
      if (item.second.size() == 1) {
        leaves.push_back(item.first);
      }
    }

    while (n > 2) {
      n -= leaves.size();
      vector<int> temp;
      for (int i : leaves) {
        auto it = adj[i].begin();
        adj[*it].erase(i);
        if (adj[*it].size() == 1) {
          temp.push_back(*it);
        }
      }
      leaves.swap(temp);
    }

    return leaves;
  }
};
// @lc code=end
