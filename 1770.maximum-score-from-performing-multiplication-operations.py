#
# @lc app=leetcode id=1770 lang=python3
#
# [1770] Maximum Score from Performing Multiplication Operations
#

# @lc code=start
from audioop import mul
from functools import cache


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        N, M = len(nums), len(multipliers)
        dp = [[0] * (M + 1) for _ in range(M + 1)]

        for pos in range(M - 1, -1, -1):
            for left in range(pos, -1, -1):
                m = multipliers[pos]
                right = N - 1 - (pos - left)
                dp[pos][left] = max(
                    m * nums[left] + dp[pos + 1][left + 1],
                    m * nums[right] + dp[pos + 1][left],
                )

        return dp[0][0]


# @lc code=end
