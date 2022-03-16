#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1 # safe to skip right
                # case 1: min is same as mid and right
                # no other values from mid to right

                # case 2: min is between mid and right
                # in this case we already know it can't be right

                # case 3: min is between left and mid
                # skip right to reduce search scope
                # can't skip left b/c it could be min, like [1,3,3]
            
        return nums[left]
# @lc code=end

