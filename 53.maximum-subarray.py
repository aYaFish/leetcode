#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        best, curr = float("-inf"), 0
        for num in nums:
            curr = max(curr + num, num)
            best = max(best, curr)

        return best


# @lc code=end
