/*
 * @lc app=leetcode id=785 lang=cpp
 *
 * [785] Is Graph Bipartite?
 */

// @lc code=start
class Solution {
 public:
  bool isBipartite(vector<vector<int>> &graph) {
    int N = graph.size();
    vector<int> color(N, -1);

    for (int i = 0; i < N; ++i) {
      // need to check color[i] is -1 to init v with color 1
      if (color[i] == -1 and !dfs(graph, color, i, 1)) {
        return false;
      }
    }
    return true;
  }

  bool dfs(vector<vector<int>> &graph, vector<int> &color, int pos, int c) {
    if (color[pos] != -1) {
      return color[pos] == c;
    }

    color[pos] = c;
    for (int v : graph[pos]) {
      if (!dfs(graph, color, v, 1 - c)) {
        return false;
      }
    }
    return true;
  }
};
// @lc code=end
