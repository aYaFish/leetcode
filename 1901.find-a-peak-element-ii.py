#
# @lc app=leetcode id=1901 lang=python3
#
# [1901] Find a Peak Element II
#

# @lc code=start
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])

        def maxRow(col: int) -> int:
            max_row = 0
            for row in range(1, ROWS):
                if mat[row][col] > mat[max_row][col]:
                    max_row = row
            return max_row

        left_col, right_col = 0, COLS - 1
        while left_col < right_col:
            mid_col = left_col + (right_col - left_col) // 2
            max_row = maxRow(mid_col)
            if mat[max_row][mid_col] > mat[max_row][mid_col + 1]:
                right_col = mid_col
            else:
                left_col = mid_col + 1

        max_row = maxRow(left_col)
        return [max_row, left_col]


# @lc code=end

