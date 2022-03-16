/*
 * @lc app=leetcode id=332 lang=cpp
 *
 * [332] Reconstruct Itinerary
 */

// @lc code=start
class Solution {
 public:
  using AirportsPQ = priority_queue<string, vector<string>, greater<string>>;
  vector<string> findItinerary(vector<vector<string>> &tickets) {
    // Find the Eulerian path, Hierholzer's Algorithm -- postorder DFS
    unordered_map<string, AirportsPQ> hash;
    for (auto &ticket : tickets) {
      hash[ticket[0]].push(ticket[1]);
    }

    vector<string> route;
    dfs("JFK", hash, route);

    reverse(route.begin(), route.end());
    return route;
  }

  void dfs(string start, unordered_map<string, AirportsPQ> &hash,
           vector<string> &route) {
    while (!hash[start].empty()) {
      string end = hash[start].top();
      hash[start].pop();
      dfs(end, hash, route);
    }
    route.push_back(start);
  }
};
// @lc code=end
