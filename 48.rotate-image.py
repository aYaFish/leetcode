#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        row = 0
        while row < N-row:
            col = row
            while col < N-row-1:
                temp = matrix[row][col]
                matrix[row][col] = matrix[N-1-col][row]
                matrix[N-1-col][row] = matrix[N-1-row][N-1-col]
                matrix[N-1-row][N-1-col] = matrix[col][N-1-row]
                matrix[col][N-1-row] = temp
                col += 1
            row += 1
        

        
# @lc code=end

