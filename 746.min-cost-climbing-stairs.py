#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(pos: int) -> int:
            if pos < 2:
                return 0
            if pos not in memo:
                memo[pos] = min(
                    dp(pos - 1) + cost[pos - 1], dp(pos - 2) + cost[pos - 2]
                )

            return memo[pos]

        return dp(len(cost))


# @lc code=end
