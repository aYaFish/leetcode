#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cash, hold = 0, -prices[0]
        for price in prices[1:]:
            cash = max(cash, hold + price)
            hold = max(hold, cash - price)

        return cash


# @lc code=end
