#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        arrows = 1
        prev_end = points[0][1]
        for start, end in points:
            if start > prev_end:
                arrows += 1
                prev_end = end
        return arrows


# @lc code=end

