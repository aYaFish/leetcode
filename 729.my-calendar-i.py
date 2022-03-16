#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
from sortedcontainers import SortedDict
class MyCalendar:

    def __init__(self):
        self.table = SortedDict() # key: start, val: end
        self.table[float("-inf")] = float("-inf")
        self.table[float("inf")] = float("inf")

    def book(self, start: int, end: int) -> bool:
        pos = self.table.bisect_left(start)
        s1, _ = self.table.peekitem(pos)
        _, e2 = self.table.peekitem(pos - 1)
        if start >= e2 and end <= s1:
            self.table[start] = end
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

