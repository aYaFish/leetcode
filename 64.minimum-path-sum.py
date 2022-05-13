#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = grid[0][:]

        for j in range(1, N):
            dp[j] += dp[j - 1]

        for i in range(1, M):
            dp[0] += grid[i][0]
            for j in range(1, N):
                dp[j] = grid[i][j] + min(dp[j], dp[j - 1])

        return dp[N - 1]


# @lc code=end
