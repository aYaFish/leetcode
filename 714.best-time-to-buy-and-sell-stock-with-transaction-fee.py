#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        dp = [[0] * 2 for _ in range(N + 1)]

        for i in range(N - 1, -1, -1):
            for holding in range(2):
                rest = dp[i + 1][holding]
                if holding == 0:
                    trade = dp[i + 1][1] - prices[i] - fee
                else:
                    trade = dp[i + 1][0] + prices[i]

                dp[i][holding] = max(rest, trade)

        return dp[0][0]


# @lc code=end
