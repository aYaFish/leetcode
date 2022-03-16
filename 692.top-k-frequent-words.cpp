/*
 * @lc app=leetcode id=692 lang=cpp
 *
 * [692] Top K Frequent Words
 */

// @lc code=start
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> counts;
        for(auto& w : words) {
            ++counts[w];
        }

        auto cmp = [&counts](string& a, string& b) {
            if(counts[a] == counts[b]) {
                // descending ordering when counts are same, so it reversed
                // back to ascending. 
                return a < b;
            }
            // min heap on counts
            return counts[a] > counts[b];
        };
        priority_queue<string, vector<string>, decltype(cmp)> pq(cmp);
        for(auto& it : counts) {
            pq.push(it.first);
            if(pq.size() > k) {
                pq.pop();
            }
        }

        vector<string> ans;
        while(!pq.empty()) {
            ans.push_back(pq.top());
            pq.pop();
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
// @lc code=end

