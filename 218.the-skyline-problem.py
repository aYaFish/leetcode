#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l, r, h in buildings:
            # corner cases:

            # same left, higher building goes first
            # same right, lower building goes first
            # the goal for above two is to set highest building first
            # on left and remove highest building last on right
            # so the following buildings sharing same left or right
            # won't make invalid change on skyline

            # left == right, left event goes first
            events += [[l, -h], [r, h]] 
        events.sort()

        ret = []
        prev = 0
        heights= SortedList([0]) # multiset in c++
        for x, h in events:
            if h < 0:
                heights.add(h)
            else:
                heights.remove(-h)
            curr = -heights[0]
            if curr != prev:
                ret.append([x, curr])
                prev = curr
        
        return ret

    # def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    #     heights = SortedDict({0: 1})
    #     points = OrderedDict()
    #     pq = [] # right, height

    #     for l, r, h in buildings:
    #         while pq and l >= pq[0][0]:
    #             x, t = heapq.heappop(pq) 
    #             heights[t] -= 1
    #             if heights[t] == 0:
    #                 heights.pop(t)
    #             points[x] = -heights.peekitem(0)[0] # key
    #         if -h in heights:
    #             heights[-h] += 1
    #         else:
    #             heights[-h] = 1
    #         points[l] = -heights.peekitem(0)[0]
    #         heapq.heappush(pq, (r, -h))
        
    #     while pq:
    #         x, t = heapq.heappop(pq) 
    #         heights[t] -= 1
    #         if heights[t] == 0:
    #             heights.pop(t)
    #         points[x] = -heights.peekitem(0)[0] # key
        
    #     prev = 0
    #     ret = []
    #     for x, h in points.items():
    #         if h != prev:
    #             ret.append([x, h])
    #         prev = h
        
    #     return ret

    # def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    #     events = [(l, -h, r) for l, r, h in buildings]
    #     events += list({(r, 0, None) for _, r, _ in buildings})
    #     events.sort() # sort by left, -height, right
    #     # for same left, highest building go first, heap is updated to highest
    #     # directly, later height won't affect heap top as they won't change
    #     # skyline
    #     # for same right, they are combined to one right in a set, the while
    #     # loop below handles all building end there

    #     ret = [[0, 0]] # x, height;
    #     pq = [(0, float("inf"))] # -height, right; inf make sure it never popped
    #     for l, neg_h, r in events:
    #         # safe to remove passed pos, it's handled below
    #         # pq top keep track valid max height
    #         # equal covers both prior end and new start of a building 
    #         # at the same position,
    #         # and prior endend only giving that end with height 0 is in events
    #         # l here could come from l in  (l,-h,r) or r in (r,0,None)
    #         # we don't care about invalid heights that are not at top
    #         # lasy clean up here when they surface to top
    #         while l >= pq[0][1]:
    #             heapq.heappop(pq)
    #         # on building left, enqueue -height, right
    #         # enqueue building start which could potentially change skyline
    #         if neg_h:
    #             heapq.heappush(pq, (neg_h, r))
    #         # order of above conditions don't matter
    #         # check if skyline has changed and update result
    #         if ret[-1][1] != -pq[0][0]:
    #             ret.append([l, -pq[0][0]])
    #     return ret[1:]

        
# @lc code=end

