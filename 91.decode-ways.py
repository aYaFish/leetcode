#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        # @cache
        # def dp(i: int) -> int:
        #     if i == 0:
        #         return 1

        #     one_back = 0
        #     if int(s[i-1:i]) > 0:
        #         one_back = dp(i-1)
        #     two_back = 0
        #     if i > 1 and 10 <= int(s[i-2:i]) <= 26:
        #         two_back = dp(i-2)

        #     return one_back + two_back

        # return dp(len(s))
        two_back = 1
        one_back = 0 if s[0] == "0" else 1

        for i in range(2, len(s) + 1):
            temp_one = 0 if s[i - 1] == "0" else one_back
            temp_two = two_back if 10 <= int(s[i - 2 : i]) <= 26 else 0
            two_back = one_back
            one_back = temp_one + temp_two

        return one_back


# @lc code=end
