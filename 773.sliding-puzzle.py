#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#

# @lc code=start
import itertools


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def neighbors(node: str):
            pos = node.index("0")
            i, j = pos // 3, pos % 3
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if x < 0 or x >= 2 or y < 0 or y >= 3:
                    continue
                left, right = pos, x * 3 + y
                if left > right:
                    left, right = right, left
                yield node[:left] + node[right] + node[left + 1 : right] + node[
                    left
                ] + node[right + 1 :]

        start = "".join(str(i) for i in itertools.chain.from_iterable(board))
        target = "123450"

        queue = deque([(start, 0)])
        seen = {start}
        while queue:
            curr, steps = queue.popleft()
            if curr == target:
                return steps

            for nei in neighbors(curr):
                if nei not in seen:
                    queue.append((nei, steps + 1))
                    seen.add(nei)

        return -1


# @lc code=end
