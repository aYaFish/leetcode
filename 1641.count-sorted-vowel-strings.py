#
# @lc app=leetcode id=1641 lang=python3
#
# [1641] Count Sorted Vowel Strings
#

# @lc code=start
class Solution:
    def countVowelStrings(self, n: int) -> int:
        # @cache
        # def backtracking(pos: int, level: int) -> int:
        #     if level == 0:
        #         return 1
        #     ans = 0
        #     for i in range(pos, 5):
        #         ans += backtracking(i, level - 1)
        #     return ans

        # return backtracking(0, n)
        dp = [[0] * 5 for _ in range(n + 1)]
        for i in range(5):
            dp[0][i] = 1

        for level in range(1, n + 1):
            for pos in range(5):
                for i in range(pos, 5):
                    dp[level][pos] += dp[level - 1][i]
        
        return dp[n][0]


            



# @lc code=end

