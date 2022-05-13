#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ans, curr_max = float("-inf"), float("-inf")
        for num in nums:
            curr_max = max(curr_max + num, num)
            ans = max(curr_max, ans)

        ans_min, curr_min = float("inf"), float("inf")
        for num in nums[1:-1]:
            curr_min = min(curr_min + num, num)
            ans_min = min(curr_min, ans_min)

        return max(ans, sum(nums) - ans_min)


# @lc code=end
