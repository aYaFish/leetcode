#
# @lc app=leetcode id=276 lang=python3
#
# [276] Paint Fence
#

# @lc code=start
from functools import cache


class Solution:
    def numWays(self, n: int, k: int) -> int:
        # @cache
        # def dp(i: int) -> int:
        #     if i == 1:
        #         return k
        #     if i == 2:
        #         return k * k
        #     return dp(i - 1) * (k - 1) + dp(i - 2) * (k - 1)

        # return dp(n)
        if k == 1:
            return 0 if n > 2 else 1

        one_back, two_back = k * k, k
        if n == 1:
            return two_back
        if n == 2:
            return one_back
        for _ in range(3, n + 1):
            temp = (k - 1) * (one_back + two_back)
            two_back = one_back
            one_back = temp

        return one_back


# @lc code=end
