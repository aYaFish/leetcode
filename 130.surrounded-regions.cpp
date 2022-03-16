/*
 * @lc app=leetcode id=130 lang=cpp
 *
 * [130] Surrounded Regions
 */

// @lc code=start
class Solution {
 public:
  vector<int> dir = {-1, 0, 1, 0, -1};
  void solve(vector<vector<char>> &board) {
    int M = board.size(), N = board[0].size();

    for (int i = 0; i < M; ++i) {
      dfs(board, i, 0);
      dfs(board, i, N - 1);
    }

    for (int j = 0; j < N; ++j) {
      dfs(board, 0, j);
      dfs(board, M - 1, j);
    }

    for (int i = 0; i < M; ++i) {
      for (int j = 0; j < N; ++j) {
        if (board[i][j] == 'M') {
          board[i][j] = 'O';
        } else {
          board[i][j] = 'X';
        }
      }
    }
  }

  void dfs(vector<vector<char>> &board, int x, int y) {
    int M = board.size(), N = board[0].size();
    if (x < 0 or x >= M or y < 0 or y >= N or board[x][y] != 'O') {
      return;
    }

    board[x][y] = 'M';
    for (int k = 0; k < 4; ++k) {
      dfs(board, x + dir[k], y + dir[k + 1]);
    }
  }
};
// @lc code=end
