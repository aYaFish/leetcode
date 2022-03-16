#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [False] * N
        dp[0] = True
        
        for i in range(1, N):
            for j in range(i-1, -1, -1):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break
        
        return dp[N-1]
                
# @lc code=end

