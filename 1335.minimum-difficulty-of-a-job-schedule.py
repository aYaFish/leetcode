#
# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
#

# @lc code=start
from functools import cache


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        if N < d:
            return -1

        # hardest_remaining = [0] * N
        # hardest = 0
        # for i in range(N - 1, -1, -1):
        #     hardest = max(hardest, jobDifficulty[i])
        #     hardest_remaining[i] = hardest

        # @cache
        # def dp(i: int, day: int):
        #     if day == d:
        #         return hardest_remaining[i]

        #     hardest = 0
        #     result = float("inf")
        #     for j in range(i, N - (d - day)):
        #         hardest = max(hardest, jobDifficulty[j])
        #         result = min(result, hardest + dp(j + 1, day + 1))

        #     return result

        # return dp(0, 1)

        dp = [[float("inf")] * (d + 1) for _ in range(N)]

        dp[-1][d] = jobDifficulty[-1]
        for i in range(N - 2, -1, -1):
            dp[i][d] = max(jobDifficulty[i], dp[i + 1][d])

        for day in range(d - 1, 0, -1):
            for i in range(day - 1, N - (d - day)):
                hardest = 0
                for j in range(i, N - (d - day)):
                    hardest = max(hardest, jobDifficulty[j])
                    dp[i][day] = min(dp[i][day], hardest + dp[j + 1][day + 1])

        return dp[0][1]


# @lc code=end
