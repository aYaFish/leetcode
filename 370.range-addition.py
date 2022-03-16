#
# @lc app=leetcode id=370 lang=python3
#
# [370] Range Addition
#

# @lc code=start
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ret = [0] * length
        nums = []
        for start, end, inc in updates:
            nums += [[start, inc], [end + 1, -inc]]
        nums.sort()
        last = val = 0
        for curr, inc in nums:
            for i in range(last, curr):
                ret[i] += val
            last = curr
            val += inc

        return ret



# @lc code=end

