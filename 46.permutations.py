#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(pos: int):
            if pos == len(nums):
                ans.append(nums[:])
                return

            for i in range(pos, len(nums)):
                nums[pos], nums[i] = nums[i], nums[pos]
                dfs(pos+1)
                nums[pos], nums[i] = nums[i], nums[pos]
            
        dfs(0)
        return ans
# @lc code=end

