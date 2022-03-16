#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in range(N)]
        dp[0] = 1

        for i in range(M):
            for j in range(N):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        
        return dp[N-1]

    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     if obstacleGrid[0][0]:
    #         return 0

    #     M, N = len(obstacleGrid), len(obstacleGrid[0])
    #     dp = [[0] * N for _ in range(M)]
    #     dp[0][0] = 1

    #     for i in range(1, M):
    #         dp[i][0] = 0 if obstacleGrid[i][0] else dp[i-1][0]
    #     for j in range(1, N):
    #         dp[0][j] = 0 if obstacleGrid[0][j] else dp[0][j-1]

    #     for i in range(1, M):
    #         for j in range(1, N):
    #             dp[i][j] = 0 if obstacleGrid[i][j] else dp[i-1][j] + dp[i][j-1]
    #     
    #     return dp[M-1][N-1]
# @lc code=end

