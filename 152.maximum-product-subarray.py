#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        # f[i]: max product that end at i
        # g[i]: min product that end at i
        # Need to track both max/min because numbers can be negative,
        # and product of two negative numbers is positive
        f, g = nums[:], nums[:]

        for i in range(1, N):
            # init state is nums[i]
            f[i] = max(f[i], nums[i]*f[i-1], nums[i]*g[i-1])
            g[i] = min(g[i], nums[i]*f[i-1], nums[i]*g[i-1])
        
        return max(f)
# @lc code=end

