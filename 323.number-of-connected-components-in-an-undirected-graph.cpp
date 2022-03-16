/*
 * @lc app=leetcode id=323 lang=cpp
 *
 * [323] Number of Connected Components in an Undirected Graph
 */

// @lc code=start
class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<int> reps(n);
        iota(reps.begin(), reps.end(), 0);

        for(auto &edge: edges) {
            combine(reps, edge[0], edge[1]);
        }

        unordered_set<int> ans;
        for(int i=0; i<n; ++i) {
            ans.insert(find(reps, i));
        }

        return ans.size();
    }

    int find(vector<int>& reps, int x) {
        if(reps[x] == x) return x;
        return reps[x] = find(reps, reps[x]);
    }

    void combine(vector<int>& reps, int x, int y) {
        reps[find(reps, x)] = find(reps, y);
    }
};
// @lc code=end

