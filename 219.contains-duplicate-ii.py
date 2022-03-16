#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = dict()
        for i, num in enumerate(nums):
            if num in hash_map:
                if i - hash_map[num] <= k:
                    return True
            hash_map[num] = i
        return False
# @lc code=end

