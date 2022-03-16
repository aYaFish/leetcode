#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
class Solution:
    # def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    #     time_lines = []
    #     for num, start, end in trips:
    #         time_lines += [[start, num], [end, -num]]
    #     time_lines.sort()
    #     total = 0
    #     for _, addition in time_lines:
    #         total += addition
    #         if total > capacity:
    #             return False
    #     return True

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        min_heap = [] # end, num
        total = 0
        for num, start, end in trips:
            while min_heap and start >= min_heap[0][0]:
                _, prev_end = heapq.heappop(min_heap)
                total -= prev_end
            heapq.heappush(min_heap, [end, num])
            total += num
            if total > capacity:
                return False
        return True


# @lc code=end

