/*
 * @lc app=leetcode id=317 lang=cpp
 *
 * [317] Shortest Distance from All Buildings
 */

// @lc code=start
class Solution {
public:
    vector<int> directions = {-1, 0, 1, 0, -1};
    int shortestDistance(vector<vector<int>>& grid) {
        int M = grid.size(), N = grid[0].size();
        vector<vector<int>> sumDistance(M, vector<int>(N, 0));

        int houseMark = 0;
        for(int i=0; i<M; ++i) {
            for(int j=0; j<N; ++j) {
                if(grid[i][j] == 1) {
                    bfs(grid, i, j, houseMark--, sumDistance);
                }
            }
        }

        int ans = INT_MAX;
        for(int i=0; i<M; ++i) {
            for(int j=0; j<N; ++j) {
                if(grid[i][j] == houseMark) {
                    ans = min(ans, sumDistance[i][j]);
                }
            }
        }

        return ans == INT_MAX ? -1 : ans;
    }

    void bfs(vector<vector<int>>& grid, int row, int col, int houseMark, vector<vector<int>>& sumDistance) {
        int M = grid.size(), N = grid[0].size();
        queue<pair<int, int>> q;
        q.push({row, col});

        int step = 0;
        while(!q.empty()) {
            ++step;
            for(int k=q.size(); k>0; --k) {
                auto curr = q.front();
                q.pop();

                int i = curr.first, j = curr.second;
                for(int d=0; d<4; ++d) {
                    int x = i+directions[d], y = j+directions[d+1];
                    if(x<0 or x>=M or y<0 or y>=N or grid[x][y] != houseMark) {
                        continue;
                    }
                    --grid[x][y];
                    sumDistance[x][y] += step;
                    q.push({x, y});
                }
            }
        }
    }

};
// @lc code=end

