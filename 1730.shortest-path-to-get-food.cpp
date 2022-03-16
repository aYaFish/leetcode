/*
 * @lc app=leetcode id=1730 lang=cpp
 *
 * [1730] Shortest Path to Get Food
 */

// @lc code=start
class Solution {
public:
    vector<int> dirs{-1, 0, 1, 0, -1};
    using Point = pair<int, int>;
    int getFood(vector<vector<char>>& grid) {
        int M = grid.size(), N = grid[0].size();
        queue<Point> q;
        
        for(int i=0; i<M; ++i) {
            for(int j=0; j<N; ++j) {
                if(grid[i][j] == '*') {
                    q.push({i, j});
                    grid[i][j] = 'X';
                    break;
                }
            }
        }

        int level = 0;
        while(!q.empty()) {
            for(int k=q.size(); k>0; --k) {
                auto curr = q.front();
                q.pop();
                for(int i=0; i<4; ++i) {
                    int x = curr.first + dirs[i], y = curr.second + dirs[i+1];
                    if(!isValid(grid, x, y)) continue;
                    if(grid[x][y] == '#') {
                        return level+1;
                    }
                    grid[x][y] = 'X';
                    q.push({x, y});
                }
            }
            ++level;
        }

        return -1;
    }

    bool isValid(vector<vector<char>>& grid, int x, int y) {
        int M = grid.size(), N = grid[0].size();
        if(x<0 or x>=M or y<0 or y>=N or grid[x][y] == 'X') {
            return false;
        }
        return true;
    }
};
// @lc code=end

