/*
 * @lc app=leetcode id=685 lang=cpp
 *
 * [685] Redundant Connection II
 */

// @lc code=start
class Solution {
 public:
  vector<int> findRedundantDirectedConnection(vector<vector<int>> &edges) {
    int N = edges.size();
    vector<int> rep(N + 1), parent(N + 1, -1);
    iota(rep.begin(), rep.end(), 0);

    int first = -1, second = -1, last = -1;
    for (int i = 0; i < N; ++i) {
      int p = edges[i][0], c = edges[i][1];
      if (parent[c] != -1) {
        first = parent[c];
        second = i;
        continue;
      }
      parent[c] = i;
      int rp = find(p, rep), rc = find(c, rep);
      if (rc == rp) {
        last = i;
      } else {
        rep[rc] = rp;
      }
    }

    if (last == -1) return edges[second];
    if (second == -1) return edges[last];
    return edges[first];
  }

  int find(int x, vector<int> &rep) {
    if (rep[x] == x) {
      return x;
    }
    return rep[x] = find(rep[x], rep);
  }
};
// @lc code=end
