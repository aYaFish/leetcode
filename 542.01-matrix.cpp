/*
 * @lc app=leetcode id=542 lang=cpp
 *
 * [542] 01 Matrix
 */

// @lc code=start
class Solution {
public:
    vector<int> directions = {-1, 0, 1, 0, -1};
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int M = mat.size(), N = mat[0].size();
        vector<vector<int>> dist(M, vector<int>(N, INT_MAX));
        queue<pair<int, int>> q;
        for(int i=0; i<M; ++i) {
            for(int j=0; j<N; ++j) {
                if(mat[i][j] == 0) {
                    dist[i][j] = 0;
                    q.push({i, j});
                }
            }
        }

        while(!q.empty()) {
            auto curr = q.front();
            q.pop();

            for(int k=0; k<4; ++k) {
                int i = curr.first + directions[k], j = curr.second + directions[k+1];
                if(i<0 or i>=M or j<0 or j>=N or dist[i][j] < dist[curr.first][curr.second]+1) {
                    continue;
                }
                dist[i][j] = dist[curr.first][curr.second]+1;
                q.push({i, j});
            }
        }

        return dist;
    }

};
// @lc code=end

