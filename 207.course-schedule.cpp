/*
 * @lc app=leetcode id=207 lang=cpp
 *
 * [207] Course Schedule
 */

// @lc code=start
class Solution {
 public:
  enum Color { white, grey, black };
  bool canFinish(int numCourses, vector<vector<int>> &prerequisites) {
    vector<vector<int>> graph(numCourses);
    vector<Color> visited(numCourses, white);
    for (auto &p : prerequisites) {
      graph[p[1]].push_back(p[0]);
    }

    for (int i = 0; i < numCourses; ++i) {
      if (visited[i] == white and !dfs(graph, i, visited)) {
        return false;
      }
    }
    return true;
  }

  bool dfs(vector<vector<int>> &graph, int i, vector<Color> &visited) {
    visited[i] = grey;
    for (auto n : graph[i]) {
      if (visited[n] == grey) {
        return false;
      } else if (visited[n] == white and !dfs(graph, n, visited)) {
        return false;
      }
    }
    visited[i] = black;
    return true;
  }
};
// @lc code=end
