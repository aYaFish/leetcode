#
# @lc app=leetcode id=1473 lang=python3
#
# [1473] Paint House III
#

# @lc code=start
class Solution:
    def minCost(
        self,
        houses: List[int],
        cost: List[List[int]],
        m: int,
        n: int,
        target: int,
    ) -> int:
        dp = [
            [[float("inf")] * (n + 1) for _ in range(target + 1)]
            for _ in range(m)
        ]
        for i in range(1, n + 1):
            if houses[0] == 0:
                dp[0][1][i] = cost[0][i - 1]
            elif i == houses[0]:
                dp[0][1][i] = 0

        for i in range(1, m):
            for j in range(1, target + 1):
                for k in range(1, n + 1):
                    if houses[i] != 0 and houses[i] != k:
                        continue
                    for c in range(1, n + 1):
                        tmp = 0 if c == k else 1
                        spend = 0 if houses[i] == k else cost[i][k - 1]
                        dp[i][j][k] = min(
                            dp[i][j][k], dp[i - 1][j - tmp][c] + spend
                        )

        ret = min(dp[m - 1][target])
        return -1 if ret == float("inf") else ret

        # @cache
        # def dp(pos: int, color: int, neighborhood: int):
        #     ans = float("inf")
        #     if pos == 0:
        #         if neighborhood != 1:
        #             return ans
        #         if houses[pos] == 0:
        #             return cost[0][color - 1]
        #         if color == houses[pos]:
        #             return 0
        #         return ans

        #     if houses[pos] != 0 and houses[pos] != color:
        #         return ans

        #     for c in range(1, n + 1):
        #         tmp = 0 if c == color else 1
        #         spend = 0 if houses[pos] == color else cost[pos][color - 1]
        #         ans = min(ans, dp(pos - 1, c, neighborhood - tmp) + spend)

        #     return ans

        # ret = min([dp(m - 1, c, target) for c in range(1, n + 1)])
        # return -1 if ret == float("inf") else ret


# @lc code=end
