#
# @lc app=leetcode id=1182 lang=python3
#
# [1182] Shortest Distance to Target Color
#

# @lc code=start
class Solution:
    def shortestDistanceColor(
        self, colors: List[int], queries: List[List[int]]
    ) -> List[int]:
        N = len(colors)
        # left -> right, right_most is the last seen index for the color
        right_most = [-1] * 3
        # right -> left, left_most is the last seen index for the color
        left_most = [N] * 3

        distance = [[-1] * N for _ in range(3)]

        for i in range(N):
            color = colors[i] - 1
            for j in range(right_most[color] + 1, i + 1):
                distance[color][j] = i - j
            right_most[color] = i

        for i in range(N - 1, -1, -1):
            color = colors[i] - 1
            for j in range(left_most[color] - 1, i - 1, -1):
                if distance[color][j] == -1 or distance[color][j] > j - i:
                    distance[color][j] = j - i
            left_most[color] = i

        return [distance[color - 1][i] for i, color in queries]


# @lc code=end
