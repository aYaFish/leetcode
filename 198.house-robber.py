#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(pos: int) -> int:
            nonlocal memo
            if pos == 0:
                return nums[0]
            if pos == 1:
                return max(nums[0], nums[1])
            if pos not in memo:
                memo[pos] = max(dp(pos - 1), dp(pos - 2) + nums[pos])

            return memo[pos]

        memo = {}
        return dp(len(nums) - 1)


# @lc code=end
