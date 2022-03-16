/*
 * @lc app=leetcode id=721 lang=cpp
 *
 * [721] Accounts Merge
 */

// @lc code=start
/*
// DFS construct a graph and find connected component
class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        unordered_map<string, string> emailToName;
        unordered_map<string, unordered_set<string>> graph;

        for(auto& acc : accounts) {
            auto& name = acc[0];
            for(int i=1; i<acc.size(); ++i) {
                graph[acc[1]].insert(acc[i]);
                graph[acc[i]].insert(acc[1]);
                emailToName[acc[i]] = name;
            }
        }

        vector<vector<string>> ans;
        unordered_set<string> visited;
        for(auto& item : graph) {
            if(visited.count(item.first)) continue;
            vector<string> temp{emailToName[item.first]};
            dfs(graph, item.first, visited, temp);
            sort(temp.begin()+1, temp.end());
            ans.emplace_back(temp);
        }

        return ans;
    }

    void dfs(unordered_map<string, unordered_set<string>>& graph,
             const string& email,
             unordered_set<string>& visited,
             vector<string>& result) {
        visited.insert(email);
        result.push_back(email);

        for(auto& e : graph[email]) {
            if(visited.count(e)) continue;
            dfs(graph, e, visited, result);
        }
    }
};
*/
// Union-Find
class Solution {
 public:
  vector<vector<string>> accountsMerge(vector<vector<string>> &accounts) {
    unordered_map<string, string> emailToName;

    for (auto &acc : accounts) {
      auto &name = acc[0];
      for (int i = 1; i < acc.size(); ++i) {
        emailToName[acc[i]] = name;
        if (!rep.count(acc[i])) {
          rep[acc[i]] = acc[i];
        }
        combine(acc[i], acc[1]);
      }
    }

    unordered_map<string, unordered_set<string>> map;
    for (auto &it : emailToName) {
      auto &r = find(it.first);
      map[r].insert(it.first);
    }

    vector<vector<string>> ans;
    for (auto &it : map) {
      vector<string> temp{emailToName[it.first]};
      temp.insert(temp.end(), it.second.begin(), it.second.end());
      sort(temp.begin() + 1, temp.end());
      ans.emplace_back(temp);
    }

    return ans;
  }

  const string &find(const string &x) {
    if (rep[x] == x) {
      return x;
    }
    return rep[x] = find(rep[x]);
  }

  void combine(const string &a, const string &b) { rep[find(a)] = find(b); }

 private:
  unordered_map<string, string> rep;
};
// @lc code=end
