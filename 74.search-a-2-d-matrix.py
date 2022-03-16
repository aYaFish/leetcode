#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])

        left = 0
        right = M*N-1
        while left < right:
            mid = (left + right) // 2
            val = matrix[mid//N][mid%N]
            if val < target:
                left = mid + 1
            else:
                right = mid
        return matrix[left//N][left%N] == target


    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     self.matrix = matrix
    #     M = len(matrix)
    #     N = len(matrix[0])
    #     self.target = target

    #     row = self.verticalSearch(0, M-1)
    #     if self.matrix[row][0] == self.target:
    #         return True
    #     col = self.horizontalSearch(row, 0, N-1)
    #     return self.matrix[row][col] == self.target


    # def verticalSearch(self, top: int, bottom: int) -> int:
    #     while top < bottom:
    #         mid = (top + bottom + 1) // 2
    #         if self.matrix[mid][0] > self.target:
    #             bottom = mid - 1
    #         else:
    #             top = mid
    #     return top

    # def horizontalSearch(self, row: int, left: int, right: int) -> int:
    #     while left < right:
    #         mid = (left + right) // 2
    #         if self.matrix[row][mid] < self.target:
    #             left = mid + 1
    #         else:
    #             right = mid
    #     return left



# @lc code=end

