#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
from typing import Tuple


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        minHeap = []

        for j in range(N):
            heapq.heappush(minHeap, (matrix[j][0], j, 0))
        
        while k:
            val, row, col = heapq.heappop(minHeap)
            if col+1 < N:
                heapq.heappush(minHeap, (matrix[row][col+1], row, col+1))
            k -= 1
        
        return val 


    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     self.matrix = matrix
    #     self.N = len(matrix)

    #     left = matrix[0][0]
    #     right = matrix[self.N-1][self.N-1]

    #     while left < right:
    #         mid = left + (right - left) // 2
    #         count, less, more = self.countLessEqual(mid)
    #         if count == k:
    #             return less
    #         elif count < k:
    #             left = more
    #         else:
    #             right = less

    #     return left

    #     
    # def countLessEqual(self, mid: int) -> Tuple[int, int, int]:
    #     row, col = self.N-1, 0
    #     more, less = self.matrix[self.N-1][self.N-1], self.matrix[0][0]
    #     count = 0
    #     while row >= 0 and col < self.N:
    #         if self.matrix[row][col] > mid:
    #             more = min(more, self.matrix[row][col])
    #             row -= 1
    #         else:
    #             less = max(less, self.matrix[row][col])
    #             count += row + 1
    #             col += 1
    #     
    #     return (count, less, more)



# @lc code=end

