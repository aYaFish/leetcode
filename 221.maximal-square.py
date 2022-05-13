#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M, N = len(matrix), len(matrix[0])

        ans = 0
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = (
                        min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    )

                    ans = max(ans, dp[i][j])

        return ans * ans


# @lc code=end
