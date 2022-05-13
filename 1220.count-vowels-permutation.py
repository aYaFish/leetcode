#
# @lc app=leetcode id=1220 lang=python3
#
# [1220] Count Vowels Permutation
#

# @lc code=start
from functools import cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[1] * 5 for _ in range(n + 1)]

        for i in range(n - 1, 0, -1):
            for j in range(5):
                if j == 0:
                    dp[i][j] = dp[i + 1][1]
                elif j == 1:
                    dp[i][j] = dp[i + 1][0] + dp[i + 1][2]
                elif j == 2:
                    dp[i][j] = 0
                    for k in range(5):
                        if k != 2:
                            dp[i][j] += dp[i + 1][k]
                elif j == 3:
                    dp[i][j] = dp[i + 1][2] + dp[i + 1][4]
                else:
                    dp[i][j] = dp[i + 1][0]
                dp[i][j] %= MOD

        return sum(dp[1][j] for j in range(5)) % MOD

        # @cache
        # def dp(pos: int, val: int):
        #     if pos == n:
        #         return 1

        #     ans = 0
        #     if val == 0:
        #         ans = dp(pos + 1, 1)
        #     elif val == 1:
        #         ans = dp(pos + 1, 0) + dp(pos + 1, 2)
        #     elif val == 2:
        #         for i in range(5):
        #             if i != 2:
        #                 ans += dp(pos + 1, i)
        #     elif val == 3:
        #         ans = dp(pos + 1, 2) + dp(pos + 1, 4)
        #     else:
        #         ans = dp(pos + 1, 0)

        #     return ans % MOD

        # return sum([dp(1, i) for i in range(5)]) % MOD


# @lc code=end
