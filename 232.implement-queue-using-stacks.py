#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start

class MyQueue:

    def __init__(self):
        self.input = deque()
        self.output = deque()

    def push(self, x: int) -> None:
        self.input.append(x)
    
    def adjust(self) -> None:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

    def pop(self) -> int:
        self.adjust()
        return self.output.pop()

    def peek(self) -> int:
        self.adjust()
        return self.output[-1]

    def empty(self) -> bool:
        return not (self.input or self.output)

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

