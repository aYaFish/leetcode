#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # N = len(prices)
        # dp = [[0] * 3 for _ in range(N + 1)]

        # for i in range(N - 1, -1, -1):
        #     for status in range(3):
        #         rest = dp[i + 1][status]
        #         if status == 0:  # not holding
        #             trade = dp[i + 1][1] - prices[i]
        #         elif status == 1:  # holding
        #             trade = dp[i + 1][2] + prices[i]
        #         else:  # status == 2 trade finished
        #             trade = 0

        #         dp[i][status] = max(trade, rest)

        # return dp[0][0]
        best, curr = 0, prices[0]
        for price in prices[1:]:
            best = max(best, price - curr)
            curr = min(curr, price)
        
        return best


# @lc code=end
