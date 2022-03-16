#
# @lc app=leetcode id=716 lang=python3
#
# [716] Max Stack
#

# @lc code=start
class MaxStack:

    def __init__(self):
        self.stack = deque()
        self.max_stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)        
        if not self.max_stack or x > self.max_stack[-1][0]:
            self.max_stack.append([x, 1])
        elif x == self.max_stack[-1][0]:
            self.max_stack[-1][1] += 1

    def pop(self) -> int:
        if self.max_stack[-1][0] == self.stack[-1]:
            self.max_stack[-1][1] -= 1

        if self.max_stack[-1][1] == 0:
            self.max_stack.pop()
        
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def peekMax(self) -> int:
        return self.max_stack[-1][0]

    def popMax(self) -> int:
        temp = deque()
        while self.peekMax() != self.stack[-1]:
            temp.append(self.pop())
        curr_max = self.pop()
        while temp:
            self.push(temp.pop())
        
        return curr_max

        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
# @lc code=end

