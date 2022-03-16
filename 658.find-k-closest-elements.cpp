/*
 * @lc app=leetcode id=658 lang=cpp
 *
 * [658] Find K Closest Elements
 */

// @lc code=start
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        auto cmp = [x](int a, int b) {
            if(abs(a-x) == abs(b-x)) {
                return a < b;
            }
            return abs(a-x) < abs(b-x);
        };
        priority_queue<int, vector<int>, decltype(cmp)> pq(cmp);
        for(int i : arr) {
            pq.push(i);
            if(pq.size() > k) {
                pq.pop();
            }
        }

        vector<int> ans;
        while(!pq.empty()) {
            ans.push_back(pq.top());
            pq.pop();
        }
        sort(ans.begin(), ans.end());

        return ans;
    }
};
// @lc code=end

