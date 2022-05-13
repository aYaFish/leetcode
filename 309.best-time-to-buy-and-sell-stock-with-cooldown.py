#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0] * 3 for _ in range(N + 1)]

        for i in range(N - 1, -1, -1):
            for status in range(3):
                rest = dp[i + 1][status]
                trade, cooldown = 0, 0
                if status == 0:  # not holding
                    trade = dp[i + 1][1] - prices[i]
                elif status == 1:  # holding
                    trade = dp[i + 1][2] + prices[i]
                else:  # status == 2 cooldown
                    cooldown = dp[i + 1][0]

                dp[i][status] = max(trade, rest, cooldown)

        return dp[0][0]
        
# @lc code=end

