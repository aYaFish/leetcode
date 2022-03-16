#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        ans = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    ans += 4
                    # remove up and left only
                    # right and down is covered by loop
                    # left to right; Top to down
                    if i > 0 and grid[i-1][j] == 1:
                        ans -= 2 # remove from both block 1+1
                    if j > 0 and grid[i][j-1] == 1:
                        ans -= 2
        
        return ans

    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    #     row, col = len(grid), len(grid[0])
    #     ans = 0

    #     def dfs(x: int, y: int) -> int:
    #         nonlocal row, col, grid, ans
    #         if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] == 0:
    #             return 0
    #         if grid[x][y] == 2:
    #             return 1

    #         grid[x][y] = 2

    #         perimeter = 4
    #         perimeter -= dfs(x-1, y)
    #         perimeter -= dfs(x+1, y)
    #         perimeter -= dfs(x, y-1)
    #         perimeter -= dfs(x, y+1)

    #         ans += perimeter

    #         return 1
    #     
    #     for i in range(row):
    #         for j in range(col):
    #             if grid[i][j] == 1:
    #                 dfs(i, j)
    #     
    #     return ans

# @lc code=end

