#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                right -= 1
        return nums[left] == target


# @lc code=end

