#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#

# @lc code=start
from sortedcontainers import SortedDict
class MyCalendarTwo:

    # def __init__(self):
    #     self.table = SortedDict()
        

    # def book(self, start: int, end: int) -> bool:
    #     self.table[start] = self.table.get(start, 0) + 1
    #     self.table[end] = self.table.get(end, 0) - 1

    #     count = 0
    #     for val in self.table.values():
    #         count += val
    #         if count >= 3:
    #             if self.table[start] == 1:
    #                 self.table.pop(start)
    #             else:
    #                 self.table[start] -= 1
    #             if self.table[end] == -1:
    #                 self.table.pop(end)
    #             else:
    #                 self.table[end] += 1
    #             return False
    #     return True

    def __init__(self):
        self.calendar = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:
        for left, right in self.overlap:
            if start < right and end > left:
                return False
        for left, right in self.calendar:
            if start < right and end > left:
                self.overlap.append((max(start, left), min(end, right)))
        self.calendar.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# @lc code=end

