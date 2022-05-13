#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
from functools import cache


class Solution:
    # def maxProfit(self, k: int, prices: List[int]) -> int:
    #     @cache
    #     def dp(i: int, remains: int, holding: bool) -> int:
    #         if remains == 0 or i == len(prices):
    #             return 0

    #         rest = dp(i + 1, remains, holding)
    #         if holding:
    #             trade = dp(i + 1, remains - 1, False) + prices[i]
    #         else:
    #             trade = dp(i + 1, remains, True) - prices[i]

    #         return max(rest, trade)

    #     return dp(0, k, False)

    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(N + 1)]

        for i in range(N - 1, -1, -1):
            for remains in range(1, k + 1):
                for holding in range(2):
                    rest = dp[i + 1][remains][holding]
                    if holding:
                        trade = dp[i + 1][remains - 1][0] + prices[i]
                    else:
                        trade = dp[i + 1][remains][1] - prices[i]

                    dp[i][remains][holding] = max(rest, trade)

        return dp[0][k][0]


# @lc code=end
