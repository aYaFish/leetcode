/*
 * @lc app=leetcode id=787 lang=cpp
 *
 * [787] Cheapest Flights Within K Stops
 */

// @lc code=start
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // Modified Bellman-Ford, we add relax one more edge from source on
        // each iteration, so we need 2 vectors. One is the result from last
        // iteration and the other is for current iteration.
        vector<vector<int>> costs(2, vector<int>(n, INT_MAX));
        costs[0][src] = costs[1][src] = 0;

        for(int i=0; i<k+1; ++i) {
            for(auto& f : flights) {
                int from = f[0], to = f[1], price = f[2];
                int curr = i&1, prev = 1-i&1;
                if(costs[prev][from] == INT_MAX) continue;
                costs[curr][to] = min(costs[curr][to], costs[prev][from]+price);
            }
        }

        // kth interation generates the final value.
        return costs[k&1][dst] == INT_MAX ? -1 : costs[k&1][dst];
    }

};
// @lc code=end

