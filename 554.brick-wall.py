#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#

# @lc code=start
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = defaultdict(int)
        for row in wall:
            for n in itertools.accumulate(row[:-1], initial=0):
                count[n] += 1
        count.pop(0)
        if not count:
            return len(wall)
        return len(wall) - max(count.values())


# @lc code=end

