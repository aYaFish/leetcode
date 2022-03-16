/*
 * @lc app=leetcode id=802 lang=cpp
 *
 * [802] Find Eventual Safe States
 */

// @lc code=start
/*
class Solution {
public:
    enum Color{white, grey, black};
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int N = graph.size();
        vector<Color> visited(N, white);

        for(int i=0; i<N; ++i) {
            if(visited[i] == white) {
                dfs(graph, i, visited);
            }
        }

        vector<int> ans;
        for(int i=0; i<N; ++i) {
            if(visited[i] == black) {
                ans.push_back(i);
            }
        }
        return ans;
    }

    bool dfs(vector<vector<int>>& graph, int x, vector<Color>& visited) {
        if(visited[x] != white) {
            return visited[x] == black;
        }
        visited[x] = grey;
        for(auto i : graph[x]) {
            if(!dfs(graph, i, visited)) {
                return false;
            }
        }

        visited[x] = black;
        return true;
    }
};
*/
class Solution {
 public:
  vector<int> eventualSafeNodes(vector<vector<int>> &graph) {
    int N = graph.size();

    vector<vector<int>> rGraph(N, vector<int>{});
    vector<int> inDegree(N, 0);
    queue<int> que;

    for (int i = 0; i < N; ++i) {
      for (int j : graph[i]) {
        rGraph[j].push_back(i);
        ++inDegree[i];
      }

      if (inDegree[i] == 0) {
        que.push(i);
      }
    }

    vector<bool> safe(N, false);
    while (!que.empty()) {
      int i = que.front();
      que.pop();

      safe[i] = true;
      for (int j : rGraph[i]) {
        if (--inDegree[j] == 0) {
          que.push(j);
        }
      }
    }

    vector<int> ans;
    for (int i = 0; i < N; ++i) {
      if (safe[i]) {
        ans.push_back(i);
      }
    }
    return ans;
  }
};
// @lc code=end
