#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr, count = 0, 1
        for peek in range(1, len(nums)):
            if nums[peek] == nums[curr]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                curr += 1
                nums[curr] = nums[peek]
        
        return curr+1
# @lc code=end

