/*
 * @lc app=leetcode id=90 lang=cpp
 *
 * [90] Subsets II
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> path;
        vector<vector<int>> ans;

        dfs(nums, 0, path, ans);
        return ans;
    }

    void dfs(vector<int>& nums, int pos, vector<int>& path, vector<vector<int>>& ans) {
        ans.push_back(path);
        if(pos == nums.size()) return;

        for(int i=pos; i<nums.size(); ++i) {
            if(i>pos and nums[i] == nums[i-1]) continue;
            path.push_back(nums[i]);
            dfs(nums, i+1, path, ans);
            path.pop_back();
        }
    }
};
// @lc code=end

