#
# @lc app=leetcode id=732 lang=python3
#
# [732] My Calendar III
#

# @lc code=start
from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.calendar = SortedDict()
        

    def book(self, start: int, end: int) -> int:
        self.calendar[start] = self.calendar.get(start, 0) + 1
        self.calendar[end] = self.calendar.get(end, 0) - 1

        ret, curr = 0, 0
        for val in self.calendar.values():
            curr += val
            ret = max(curr, ret)
        
        return ret

        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
# @lc code=end

