#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def dp(pos: int) -> int:
            if pos == 0:
                return 0
            if pos < 3:
                return 1
            if pos not in memo:
                memo[pos] = dp(pos - 1) + dp(pos - 2) + dp(pos - 3)
            return memo[pos]

        return dp(n)


# @lc code=end
