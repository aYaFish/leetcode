#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for left, right in intervals:
            end = result[-1][1]
            if left <= end:
                result[-1][1] = max(right, end)
            else:
                result.append([left, right])
            
        return result
        
# @lc code=end

