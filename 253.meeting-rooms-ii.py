#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end_times = []
        rooms = 0
        for start, end in intervals:
            while end_times and start >= end_times[0]:
                heapq.heappop(end_times)
            heapq.heappush(end_times, end)
            rooms = max(rooms, len(end_times))
        return rooms

    # def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    #     time_line = []
    #     for start, end in intervals:
    #         time_line += [[start, 1], [end, -1]]
    #     time_line.sort() # end comes before start on equal so -1 before +1
    #     ret = count = 0
    #     for _, increment in time_line:
    #         count += increment
    #         ret = max(ret, count)
    #     return ret

# @lc code=end

