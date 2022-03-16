#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {}

        def dfs(remain: int) -> int:
            if remain == 0:
                return 1
            if remain in memo:
                return memo[remain]
            
            count = 0
            for i in range(0, len(nums)):
                if nums[i] > remain:
                    break
                count += dfs(remain - nums[i])
            
            memo[remain] = count
            return count
        
        return dfs(target)


        
# @lc code=end

