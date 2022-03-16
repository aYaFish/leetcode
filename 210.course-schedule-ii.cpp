/*
 * @lc app=leetcode id=210 lang=cpp
 *
 * [210] Course Schedule II
 */

// @lc code=start
class Solution {
 public:
  enum Color { white, grey, black };
  vector<int> findOrder(int numCourses, vector<vector<int>> &prerequisites) {
    vector<vector<int>> graph(numCourses);
    vector<Color> record(numCourses, white);
    vector<int> ans;

    for (auto &p : prerequisites) {
      graph[p[1]].push_back(p[0]);
    }

    for (int i = 0; i < numCourses; ++i) {
      if (record[i] == white and !dfs(graph, i, record, ans)) {
        return {};
      }
    }

    reverse(ans.begin(), ans.end());
    return ans;
  }

  bool dfs(vector<vector<int>> &graph, int i, vector<Color> &record,
           vector<int> &ans) {
    record[i] = grey;
    for (int j : graph[i]) {
      if (record[j] == grey) {
        return false;
      } else if (record[j] == white and !dfs(graph, j, record, ans)) {
        return false;
      }
    }
    record[i] = black;
    ans.push_back(i);
    return true;
  }
};
// @lc code=end
