#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (1, -1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

        start = "0000"
        seen = set(deadends)

        if start in seen:
            return -1

        queue = deque([(start, 0)])
        seen.add(start)
        while queue:
            curr, steps = queue.popleft()
            if curr == target:
                return steps
            for nei in neighbors(curr):
                if nei not in seen:
                    queue.append((nei, steps+1))
                    seen.add(nei)
        
        return -1

# @lc code=end

