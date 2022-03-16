#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def dfs(nums, pos):
            ans.append(list(path))
            if pos == len(nums):
                return
            for i in range(pos, len(nums)):
                path.append(nums[i])
                dfs(nums, i+1)
                path.pop()
        
        dfs(nums, 0)
        return ans
        
# @lc code=end

