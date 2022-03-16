#
# @lc app=leetcode id=694 lang=python3
#
# [694] Number of Distinct Islands
#

# @lc code=start
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0]) # len() is O(1)

        def dfs(row, col, direction):
            if 0 <= row < M and 0 <= col < N and grid[row][col]:
                grid[row][col] = 0
                path.append(direction)
                dfs(row, col+1, "u")
                dfs(row, col-1, "d")
                dfs(row-1, col, "l")
                dfs(row+1, col, "r")
                path.append("b") # need to track the way back

        unique_islands = set()
        for row in range(M):
            for col in range(N):
                path = [] #
                dfs(row, col, "s")
                if path:
                    # list is not hashable
                    unique_islands.add(tuple(path))

        return len(unique_islands)


# @lc code=end

