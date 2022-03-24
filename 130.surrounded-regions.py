#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        def dfs(x: int, y: int) -> None:
            nonlocal board
            if x < 0 or x >= M or y < 0 or y >= N or board[x][y] != "O":
                return
            board[x][y] = "M"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        for i in range(M):
            dfs(i, 0)
            dfs(i, N - 1)
        
        for j in range(N):
            dfs(0, j)
            dfs(M - 1, j)
        
        for i in range(M):
            for j in range(N):
                if board[i][j] == "M":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

        
# @lc code=end

