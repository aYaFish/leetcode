#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M, N, K = len(s1), len(s2), len(s3)
        if M + N != K:
            return False
        
        @cache
        def dp(k: int, m: int) -> bool:
            if k == K:
                return True
            
            n = k - m
            ans = False
            if m < M and s1[m] == s3[k]:
                ans |= dp(k+1, m+1)
            if n < N and s2[n] == s3[k]:
                ans |= dp(k+1, m)
            
            return ans
        
        return dp(0, 0)



        
# @lc code=end

