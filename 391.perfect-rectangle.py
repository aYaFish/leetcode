#
# @lc app=leetcode id=391 lang=python3
#
# [391] Perfect Rectangle
#

# @lc code=start
from sortedcontainers import SortedList


class Solution:
    # def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
    #     events = []
    #     bottom, top = float("inf"), float("-inf")
    #     for x, y, a, b in rectangles:
    #         # remove(-1) before add(1)
    #         events += [[x, 1, y, b], [a, -1, y, b]]
    #         bottom = min(bottom, y)
    #         top = max(top, b)
    #     events.sort()

    #     curr_x, interval = events[0][0], 0
    #     # bisect_right will never be 0, safe to -1
    #     # it will never go beyond top, safe to use pos directly
    #     # inverval and SortedList together to check gap or overlap
    #     # inverval to check gap, SL to check overlap
    #     verticals = SortedList([[float("-inf"), bottom], [top, float("inf")]])
    #     for x, sign, low, high in events:
    #         if x != curr_x:
    #             if interval != top - bottom:
    #                 return False
    #             curr_x = x

    #         if sign == -1:
    #             verticals.remove([low, high])
    #             interval -= high - low
    #         else:
    #             pos = verticals.bisect_right([low, high])
    #             (down1, up1), (down2, up2) = verticals[pos - 1], verticals[pos]
    #             if low < up1 or high > down2:
    #                 return False
    #             verticals.add([low, high])
    #             interval += high - low

    #     return interval == 0

    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # total area should equal to sum of single rectangle areas
        # except for 4 corners, all points count should be even (2 or 4)
        # count == (1, Corner), (2, T-junctions), (4, Cross)
        left, right, down, up = (
            float("inf"),
            float("-inf"),
            float("inf"),
            float("-inf"),
        )
        total_area = 0
        points = set()

        for x, y, a, b in rectangles:
            left = min(left, x)
            right = max(right, a)
            down = min(down, y)
            up = max(up, b)

            total_area += (a - x) * (b - y)
            if (x, y) in points:
                points.remove((x, y))
            else:
                points.add((x, y))
            if (x, b) in points:
                points.remove((x, b))
            else:
                points.add((x, b))
            if (a, y) in points:
                points.remove((a, y))
            else:
                points.add((a, y))
            if (a, b) in points:
                points.remove((a, b))
            else:
                points.add((a, b))

        if any(
            p not in points
            for p in [(left, down), (left, up), (right, down), (right, up)]
        ) or len(points) != 4:
            return False
        return total_area == (right - left) * (up - down)


# @lc code=end
