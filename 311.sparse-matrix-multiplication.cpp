/*
 * @lc app=leetcode id=311 lang=cpp
 *
 * [311] Sparse Matrix Multiplication
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& mat1, vector<vector<int>>& mat2) {
        int M = mat1.size(), K = mat1[0].size(), N = mat2[0].size();
        vector<vector<int>> ans(M, vector<int>(N, 0));

        for(int i=0; i<M; ++i) {
            for(int k=0; k<K; ++k) {
                if(mat1[i][k] == 0) continue;
                for(int j=0; j<N; ++j) {
                    if(mat2[k][j] == 0) continue;
                    ans[i][j] += mat1[i][k] * mat2[k][j];
                }
            }
        }

        return ans;
    }
};
// @lc code=end

