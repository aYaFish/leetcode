#
# @lc app=leetcode id=379 lang=python3
#
# [379] Design Phone Directory
#

# @lc code=start
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.MAXNUMBERS = maxNumbers
        self.next = 0
        self.recycle = set()

    def get(self) -> int:
        ret = -1
        if self.recycle:
            ret = self.recycle.pop()
        elif self.next < self.MAXNUMBERS:
            ret = self.next
            self.next += 1
        return ret

    def check(self, number: int) -> bool:
        return number >= self.next or number in self.recycle

    def release(self, number: int) -> None:
        if number >= self.next:
            return
        if number not in self.recycle:
            self.recycle.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
# @lc code=end

