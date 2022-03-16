/*
 * @lc app=leetcode id=815 lang=cpp
 *
 * [815] Bus Routes
 */

// @lc code=start
class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        unordered_map<int, unordered_set<int>> bus, stop, graph;
        for(int i=0; i<routes.size(); ++i) {
            bus[i] = unordered_set<int>(routes[i].begin(), routes[i].end());
        }

        for(auto& it : bus) {
            for(auto s : it.second) {
                stop[s].insert(it.first);
            }
        }

        for(auto& it : stop) {
            for(auto b : it.second) {
                for(auto c : it.second) {
                    graph[b].insert(c);
                    graph[c].insert(b);
                }
            }
        }

        if(stop.count(source) == 0 or stop.count(target) == 0) {
            return -1;
        }
        if(source == target) return 0;

        queue<int> q;
        unordered_set<int> visited;
        for(auto b : stop[source]) {
            visited.insert(b);
            q.push(b);
        }

        int ans = 0;
        while(!q.empty()) {
            ++ans;
            for(int i=q.size(); i>0; --i) {
                int b = q.front();
                q.pop();

                if(stop[target].count(b)) {
                    return ans;
                }

                for(auto v: graph[b]) {
                    if(!visited.count(v)) {
                        visited.insert(v);
                        q.push(v);
                    }
                }
            }
        }

        return -1; 
    }
};
// @lc code=end

