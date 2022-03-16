/*
 * @lc app=leetcode id=417 lang=cpp
 *
 * [417] Pacific Atlantic Water Flow
 */

// @lc code=start
class Solution {
 public:
  vector<int> dirs = {-1, 0, 1, 0, -1};
  vector<vector<int>> pacificAtlantic(vector<vector<int>> &heights) {
    int M = heights.size(), N = heights[0].size();
    vector<vector<int>> visited(M, vector<int>(N, 0));

    for (int i = 0; i < M; ++i) {
      dfs(heights, i, 0, 1, visited);
      dfs(heights, i, N - 1, 2, visited);
    }

    for (int j = 0; j < N; ++j) {
      dfs(heights, 0, j, 1, visited);
      dfs(heights, M - 1, j, 2, visited);
    }

    vector<vector<int>> ans;
    for (int i = 0; i < M; ++i) {
      for (int j = 0; j < N; ++j) {
        if (visited[i][j] == 3) {
          ans.emplace_back(vector<int>{i, j});
        }
      }
    }
    return ans;
  }

  void dfs(vector<vector<int>> &heights, int x, int y, int val,
           vector<vector<int>> &visited) {
    int M = heights.size(), N = heights[0].size();
    if (visited[x][y] & val) return;

    visited[x][y] |= val;
    for (int k = 0; k < 4; ++k) {
      int i = x + dirs[k], j = y + dirs[k + 1];
      if (i < 0 or i >= M or j < 0 or j >= N or heights[i][j] < heights[x][y]) {
        continue;
      }
      dfs(heights, i, j, val, visited);
    }
  }
};
// @lc code=end
