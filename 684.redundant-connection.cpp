/*
 * @lc app=leetcode id=684 lang=cpp
 *
 * [684] Redundant Connection
 */

// @lc code=start
class Solution {
 public:
  vector<int> findRedundantConnection(vector<vector<int>> &edges) {
    int N = edges.size();
    vector<int> rep(N + 1);
    iota(rep.begin(), rep.end(), 0);

    for (auto &e : edges) {
      if (!combine(e[0], e[1], rep)) {
        return {e[0], e[1]};
      }
    }

    return {};
  }

  int find(int x, vector<int> &rep) {
    if (rep[x] == x) {
      return x;
    }
    return rep[x] = find(rep[x], rep);
  }

  bool combine(int x, int y, vector<int> &rep) {
    int i = find(x, rep);
    int j = find(y, rep);

    if (i == j) return false;
    rep[i] = j;
    return true;
  }
};
// @lc code=end
