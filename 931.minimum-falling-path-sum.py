#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
from functools import cache


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        dp = [x[:] for x in matrix]

        for i in range(1, N):
            for j in range(N):
                dp[i][j] += min(
                    dp[i - 1][j],
                    dp[i - 1][max(0, j - 1)],
                    dp[i - 1][min(N - 1, j + 1)],
                )

        return min(dp[N - 1])

        # @cache
        # def dp(row: int, col: int):
        #     if col < 0 or col >= N:
        #         return float('inf')
        #     if row == 0:
        #         return matrix[0][col]
        #     return matrix[row][col] + min(
        #         dp(row - 1, col - 1), dp(row - 1, col), dp(row - 1, col + 1)
        #     )

        # return min([dp(N - 1, j) for j in range(N)])


# @lc code=end
