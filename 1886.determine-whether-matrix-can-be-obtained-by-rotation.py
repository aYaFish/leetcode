#
# @lc app=leetcode id=1886 lang=python3
#
# [1886] Determine Whether Matrix Can Be Obtained By Rotation
#

# @lc code=start
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        result = [True]*4 # 0, 90, 180, 270 degree rotations
        N = len(mat)
        for row in range(N):
            for col in range(N):
                if mat[row][col] != target[row][col]:
                    result[0] = False
                if mat[row][col] != target[col][N-1-row]:
                    result[1] = False
                if mat[row][col] != target[N-1-row][N-1-col]:
                    result[2] = False
                if mat[row][col] != target[N-1-col][row]:
                    result[3] = False

        return any(result)
# @lc code=end

