#
# @lc app=leetcode id=311 lang=python3
#
# [311] Sparse Matrix Multiplication
#

# @lc code=start
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        M, K, N = len(mat1), len(mat1[0]), len(mat2[0])
        ans = [[0 for _ in range(N)] for _ in range(M)]

        # for i in range(M):
        #     for k in range(K):
        #         if mat1[i][k] == 0:
        #             continue
        #         for j in range(N):
        #             if mat2[k][j] == 0:
        #                 continue
        #             ans[i][j] += mat1[i][k] * mat2[k][j]

        m1 = []
        for i in range(M):
            tmp = []
            for k in range(K):
                if mat1[i][k] != 0:
                    tmp.append((k, mat1[i][k]))

            m1.append(tmp)
        
        for i in range(M):
            for p in m1[i]:
                if not p:
                    continue
                k, val = p
                for j in range(N):
                    ans[i][j] += val * mat2[k][j] 
        
        return ans

# @lc code=end

