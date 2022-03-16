#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])

        row = M-1
        col = 0
        while row >= 0 and col < N:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        return False
# @lc code=end

