/*
 * @lc app=leetcode id=694 lang=cpp
 *
 * [694] Number of Distinct Islands
 */

// @lc code=start
class Solution {
public:
    using Point = pair<int, int>;
    vector<int> dirs = {-1, 0, 1, 0, -1};
    int numDistinctIslands(vector<vector<int>>& grid) {
        int M = grid.size(), N = grid[0].size();

        unordered_set<string> ans;
        for(int i=0; i<M; ++i) {
            for(int j=0; j<N; ++j) {
                if(!isValid(grid, i, j)) continue;
                vector<Point> island;
                bfs(grid, i, j, island);
                ans.insert(normalize(island));
            }
        }

        return ans.size();
    }

    bool isValid(vector<vector<int>>& grid, int x, int y) {
        int M = grid.size(), N = grid[0].size();
        if(x < 0 or x >= M or y < 0 or y >= N or grid[x][y] != 1) {
            return false;
        }
        return true;
    }

    void bfs(vector<vector<int>>& grid, int x, int y, vector<Point>& island) {
        queue<Point> q;
        q.push({x, y});
        grid[x][y] = 2;

        while(!q.empty()) {
            auto curr = q.front();
            q.pop();
            island.push_back({curr.first, curr.second});

            for(int k=0; k<4; ++k) {
                int i = curr.first+dirs[k], j = curr.second+dirs[k+1];
                if(!isValid(grid, i, j)) continue;
                q.push({i, j});
                grid[i][j] = 2;
            }
        }
    }

    string normalize(vector<Point>& island) {
        sort(island.begin(), island.end());
        int x0 = island[0].first, y0 = island[0].second;
        for(auto& p : island) {
            p.first -= x0;
            p.second -= y0;
        }

        stringstream ss;
        for(auto& p : island) {
            ss << p.first << ',' << p.second << ';';
        }

        return ss.str();
    }
};
// @lc code=end

