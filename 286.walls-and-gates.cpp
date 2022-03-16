/*
 * @lc app=leetcode id=286 lang=cpp
 *
 * [286] Walls and Gates
 */

// @lc code=start
class Solution {
public:
    vector<int> directs = {-1, 0, 1, 0, -1};
    void wallsAndGates(vector<vector<int>>& rooms) {
        int M = rooms.size(), N = rooms[0].size();
        queue<pair<int, int>> q;
        
        for(int i=0; i<M; ++i) {
            for(int j=0; j<N; ++j) {
                if(rooms[i][j] == 0) {
                    q.push({i, j});
                }
            }
        }

        while(!q.empty()) {
            auto curr = q.front();
            q.pop();

            for(int k=0; k<4; ++k) {
                int x = curr.first + directs[k], y = curr.second + directs[k+1];
                if(x<0 or x>=M or y<0 or y>=N or rooms[x][y] <= rooms[curr.first][curr.second]+1) {
                    continue;
                }
                rooms[x][y] = rooms[curr.first][curr.second]+1;
                q.push({x, y});
            }
        }
    }
};
// @lc code=end

