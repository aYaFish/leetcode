/*
 * @lc app=leetcode id=78 lang=cpp
 *
 * [78] Subsets
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> path;
        vector<vector<int>> ans;

        dfs(nums, 0, path, ans);
        return ans;
    }

    void dfs(vector<int>& nums, int pos, vector<int>& path, vector<vector<int>>& ans) {
        ans.push_back(path);
        if(pos == nums.size()) return;

        for(int i=pos; i<nums.size(); ++i) {
            path.push_back(nums[i]);
            dfs(nums, i+1, path, ans);
            path.pop_back();
        }
    }
};
// @lc code=end

