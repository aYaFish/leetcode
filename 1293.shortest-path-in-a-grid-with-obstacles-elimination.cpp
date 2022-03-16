/*
 * @lc app=leetcode id=1293 lang=cpp
 *
 * [1293] Shortest Path in a Grid with Obstacles Elimination
 */

// @lc code=start
class Solution {
public:
    vector<int> dirs{-1, 0, 1, 0, -1};
    using State = vector<int>;
    int shortestPath(vector<vector<int>>& grid, int k) {
        int M = grid.size(), N = grid[0].size();
        vector<vector<vector<int>>> steps(M, vector<vector<int>>(N, vector<int>(k+1, INT_MAX)));

        queue<State> q;
        q.push({0, 0, k});
        steps[0][0][k] = 0;

        while(!q.empty()) {
            auto curr = q.front();
            q.pop();

            int row = curr[0], col = curr[1], rk = curr[2];

            if(row == M-1 and col == N-1) {
                return steps[row][col][rk];
            }

            for(int t=0; t<4; ++t) {
                int nr = row+dirs[t], nc = col+dirs[t+1];
                if(nr < 0 or nr >= M or nc < 0 or nc >= N) continue;
                int nk = rk - grid[nr][nc];
                if(nk >= 0 and steps[nr][nc][nk] == INT_MAX) {
                    steps[nr][nc][nk] = steps[row][col][rk] + 1;
                    q.push({nr, nc, nk});
                }
            }
        }

        return -1;

    }

};
// @lc code=end

