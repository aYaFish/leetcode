#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#
from collections import Counter

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = [(0, 0)] + sorted(list(Counter(nums).items()))
        memo = {}

        def dp(pos: int) -> int:
            if pos < 2:
                return counter[pos][0] * counter[pos][1]
            if not pos in memo:
                val, count = counter[pos]
                if val == counter[pos - 1][0] + 1:
                    memo[pos] = max(dp(pos - 2) + val * count, dp(pos - 1))
                else:
                    memo[pos] = dp(pos - 1) + val * count
            return memo[pos]

        return dp(len(counter) - 1)


# @lc code=end
