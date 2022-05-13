#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_back, two_back = 0, 0

        for i in range(2, len(cost) + 1):
            temp = min(one_back + cost[i - 1], two_back + cost[i - 2])
            two_back = one_back
            one_back = temp

        return one_back


# @lc code=end
