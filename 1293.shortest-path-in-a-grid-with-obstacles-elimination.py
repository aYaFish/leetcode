#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

# @lc code=start
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        target = (M-1, N-1)

        def manhattan_distance(row: int, col: int) -> int:
            return target[0]-row+target[1]-col
        
        # (row, col, remain_eliminations)
        state = (0, 0, k)

        # (estimation, steps, state)
        # h(n) = manhattan_distance, g(n) = steps
        queue = [(manhattan_distance(0, 0), 0, state)]
        seen = set([state])

        while queue:
            estimation, steps, (row, col, remain_eliminations) = heapq.heappop(queue)

            # we can reach the target in the shortest path (manhattan distance),
            #   even if the remaining steps are all obstacles
            if estimation - steps <= remain_eliminations:
                return estimation
            
            # explore the four directions in the next step
            for new_row, new_col in [(row, col+1), (row+1, col), (row, col-1), (row-1, col)]:
                if (0 <= new_row < M) and (0 <= new_col < N):
                    new_eliminations = remain_eliminations - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_eliminations)

                    if new_eliminations >= 0 and new_state not in seen:
                        seen.add(new_state)
                        new_estimation = manhattan_distance(new_row, new_col)+steps+1
                        heapq.heappush(queue, (new_estimation, steps+1, new_state))

        return -1



# @lc code=end

