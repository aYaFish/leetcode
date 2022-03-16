/*
 * @lc app=leetcode id=301 lang=cpp
 *
 * [301] Remove Invalid Parentheses
 */

// @lc code=start
class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        vector<string> ans;
        string curr;

        dfs(s, 0, curr, 0, 0, ans);
        unordered_set<string> temp(ans.begin(), ans.end());
        ans.assign(temp.begin(), temp.end());

        return ans;
    }

    void dfs(const string& s, int pos, string& curr, int open_count, int close_count, vector<string>& ans) {
        if(pos == s.size()) {
            if(open_count != close_count) return;
            if(ans.empty()) {
                ans.push_back(curr);
                return;
            }
            int l = ans.front().size();
            if(curr.size() >= l) {
                if(curr.size() > l) {
                    ans.clear();
                }
                ans.push_back(curr);
            }
            return;
        }
        if(s[pos] != '(' and s[pos] != ')') {
            curr.push_back(s[pos]);
            dfs(s, pos+1, curr, open_count, close_count, ans);
            curr.pop_back();
        }
        else {
            dfs(s, pos+1, curr, open_count, close_count, ans);
            if(s[pos] == '(') {
                curr.push_back(s[pos]);
                dfs(s, pos+1, curr, open_count+1, close_count, ans);
                curr.pop_back();
            }
            else if(open_count > close_count) {
                curr.push_back(s[pos]);
                dfs(s, pos+1, curr, open_count, close_count+1, ans);
                curr.pop_back();
            }
        }
    }
};
// @lc code=end

