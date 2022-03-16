#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        seen = [[False] * N for _ in range(M)]

        def dfs(i: int, j: int, pos: int) -> bool:
            nonlocal seen
            if pos == len(word):
                return True
            seen[i][j] = True
            ans = False
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if (
                    x < 0
                    or x >= M
                    or y < 0
                    or y >= N
                    or seen[x][y]
                    or board[x][y] != word[pos]
                ):
                    continue
                ans = dfs(x, y, pos + 1)
                if ans:
                    break
            seen[i][j] = False
            return ans

        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0] and dfs(i, j, 1):
                    return True
        return False


# @lc code=end
