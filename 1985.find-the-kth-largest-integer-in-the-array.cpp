/*
 * @lc app=leetcode id=1985 lang=cpp
 *
 * [1985] Find the Kth Largest Integer in the Array
 */

// @lc code=start
class Solution {
public:
    string kthLargestNumber(vector<string>& nums, int k) {
        auto cmp = [](string& a, string& b) {
            if(a.size() != b.size()) {
                return a.size() > b.size();
            }
            return a > b;
        };
        priority_queue<string, vector<string>, decltype(cmp)> pq(cmp);

        for(auto& s : nums) {
            pq.push(s);
            if(pq.size() > k) {
                pq.pop();
            }
        }

        return pq.top();
    }
};
// @lc code=end

