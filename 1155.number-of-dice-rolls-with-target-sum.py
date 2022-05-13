#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#

# @lc code=start
from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for val in range(1, k + 1):
                for t in range(val, target + 1):
                    dp[i][t] = (dp[i][t] + dp[i - 1][t - val]) % MOD
        return dp[n][target] % MOD

        # @cache
        # def dp(dices: int, remaining: int):
        #     if dices == 0:
        #         if remaining == 0:
        #             return 1
        #         return 0
        #     if remaining < 0:
        #         return 0

        #     ans = 0
        #     for i in range(1, k + 1):
        #         ans += dp(dices - 1, remaining - i)

        #     return ans % MOD

        # return dp(n, target) % MOD


# @lc code=end
