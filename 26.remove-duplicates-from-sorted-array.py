#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr = 0
        for peek in range(1, len(nums)):
            if nums[peek] == nums[curr]:
                continue
            curr += 1
            nums[curr] = nums[peek]

        return curr + 1
# @lc code=end

