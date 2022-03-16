#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = len(nums) * (len(nums) + 1) // 2
        return expected_sum - sum(nums)

        
# @lc code=end

