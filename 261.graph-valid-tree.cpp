/*
 * @lc app=leetcode id=261 lang=cpp
 *
 * [261] Graph Valid Tree
 */

// @lc code=start
class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        vector<int> reps(n);
        iota(reps.begin(), reps.end(), 0);

        for(auto& e : edges) {
            if(combine(e[0], e[1], reps) == false) {
                return false;
            }
        }
        return edges.size()+1 == n;
    }

    int find(int x, vector<int>& reps) {
        if(reps[x] == x) return x;
        return reps[x] = find(reps[x], reps);
    }

    bool combine(int x, int y, vector<int>& reps) {
        int rx = find(x, reps), ry = find(y, reps);
        if(rx == ry) return false;
        reps[ry] = rx;
        return true;
    }
};
// @lc code=end

