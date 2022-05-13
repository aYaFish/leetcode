#
# @lc app=leetcode id=265 lang=python3
#
# [265] Paint House II
#

# @lc code=start
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        N, K = len(costs), len(costs[0])
        dp = [x[:] for x in costs]

        for i in range(1, N):
            for j in range(K):
                dp[i][j] = float("inf")
                for k in range(K):
                    if j == k:
                        continue
                    dp[i][j] = min(dp[i][j], dp[i - 1][k])
                dp[i][j] += costs[i][j]

        return min(dp[N - 1])


# @lc code=end
