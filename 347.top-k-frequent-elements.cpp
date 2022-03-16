/*
 * @lc app=leetcode id=347 lang=cpp
 *
 * [347] Top K Frequent Elements
 */

// @lc code=start
class Solution {
public:
    using Element = pair<int, int>;
    vector<int> topKFrequent(vector<int>& nums, int k) {
        auto cmp = [](const Element& a, const Element& b) {
            if(a.second == b.second) {
                return a.first < b.first;
            }
            return a.second < b.second;
        };
        set<Element, decltype(cmp)> pq(cmp);
        unordered_map<int, int> hash;

        for(auto i : nums) {
            if(hash.count(i) != 0) {
                pq.erase({i, hash[i]});
            }
            ++hash[i];
            pq.insert({i, hash[i]});
            if(pq.size() > k) {
                pq.erase(pq.begin());
            }
        }
        
        vector<int> ans;
        for(auto& it : pq) {
            ans.push_back(it.first);
        }

        return ans;
    }
};
// @lc code=end

