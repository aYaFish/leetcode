#
# @lc app=leetcode id=256 lang=python3
#
# [256] Paint House
#

# @lc code=start
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        dp = [x[:] for x in costs]

        for i in range(1, N):
            for j in range(3):
                dp[i][j] = float("inf")
                for c in range(3):
                    if j == c:
                        continue
                    dp[i][j] = min(dp[i][j], dp[i - 1][c])
                dp[i][j] += costs[i][j]

        return min(dp[N - 1])


# @lc code=end
