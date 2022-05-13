#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#

# @lc code=start
from functools import cache


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [[0] * (amount + 1) for _ in range(N + 1)]

        for i in range(N + 1):
            dp[i][0] = 1

        for i in range(1, N + 1):
            coin = coins[i - 1]
            for remain in range(amount + 1):
                if remain < coin:
                    dp[i][remain] = dp[i - 1][remain]
                else:
                    dp[i][remain] = dp[i - 1][remain] + dp[i][remain - coin]

        return dp[N][amount]

        # dp = [0] * (amount + 1)
        # dp[0] = 1

        # for c in coins:
        #     for x in range(c, amount + 1):
        #         dp[x] += dp[x - c]

        # return dp[amount]

        # @cache
        # def dp(remaining: int, i: int) -> int:
        #     if remaining < 0 or i == len(coins):
        #         return 0
        #     if remaining == 0:
        #         return 1

        #     return dp(remaining - coins[i], i) + dp(remaining, i + 1)

        # return dp(amount, 0)


# @lc code=end
