#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        counts = [-1] * N
        sorted_list = SortedList()

        for i in range(N - 1, -1, -1):
            num = nums[i]
            counts[i] = sorted_list.bisect_left(num)
            sorted_list.add(num)

        return counts


# @lc code=end
