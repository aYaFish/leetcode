/*
 * @lc app=leetcode id=254 lang=cpp
 *
 * [254] Factor Combinations
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> getFactors(int n) {
        vector<vector<int>> ans;
        vector<int> path;

        dfs(n, 2, path, ans);

        return ans;
    }

    void dfs(int quo, int div, vector<int>& path, vector<vector<int>>& ans) {
        for(int i=div; i<=quo/i; ++i) {
            if(quo % i == 0) {
                path.push_back(i);
                ans.push_back(path);
                ans.rbegin()->push_back(quo/i);

                dfs(quo/i, i, path, ans);
                path.pop_back();
            }
        }
    }
};
// @lc code=end

