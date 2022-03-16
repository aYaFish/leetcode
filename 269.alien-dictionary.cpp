/*
 * @lc app=leetcode id=269 lang=cpp
 *
 * [269] Alien Dictionary
 */

// @lc code=start
class Solution {
 public:
  enum Color { WHITE, GREY, BLACK };
  string alienOrder(vector<string> &words) {
    unordered_map<char, vector<char>> rGraph;

    for (auto &w : words) {
      for (char c : w) {
        rGraph[c];
      }
    }

    for (int i = 0; i < words.size() - 1; ++i) {
      string &w1 = words[i], w2 = words[i + 1];
      if (w1.size() > w2.size() and w1.find(w2) == 0) {
        return "";
      }

      for (int j = 0; j < min(w1.size(), w2.size()); ++j) {
        if (w1[j] != w2[j]) {
          rGraph[w2[j]].push_back(w1[j]);
          break;
        }
      }
    }

    // Different approach to implement WHITE, GREY, BLACK
    // WHITE -> not in map
    // GREY -> false value in map
    // BLACK -> true value in map
    unordered_map<char, bool> visited;
    string ans;

    for (auto &it : rGraph) {
      if (!dfs(rGraph, it.first, visited, ans)) {
        return "";
      }
    }

    return ans;
  }

  bool dfs(unordered_map<char, vector<char>> &rGraph, char c,
           unordered_map<char, bool> &visited, string &ans) {
    if (visited.count(c)) {
      return visited[c];
    }
    visited[c] = false;
    for (char r : rGraph[c]) {
      if (!dfs(rGraph, r, visited, ans)) {
        return false;
      }
    }

    visited[c] = true;
    ans.push_back(c);
    return true;
  }
};
// @lc code=end
