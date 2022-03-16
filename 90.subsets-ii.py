#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        ans = []

        def dfs(nums, pos):
            ans.append(path[:])
            if pos == len(nums):
                return
            
            for i in range(pos, len(nums)):
                if i>pos and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(nums, i+1)
                path.pop()

        dfs(nums, 0)
        return ans

    def subsetsSizeKWithDup(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        path = []
        ans = []

        def dfs(nums, pos):
            if len(path) == k:
                ans.append(path[:])
                return
            if pos == len(nums):
                return
            
            for i in range(pos, len(nums)):
                if i>pos and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(nums, i+1)
                path.pop()

        dfs(nums, 0)
        return ans

    def subsetsNoNeighborWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        ans = []

        def dfs(nums, pos):
            ans.append(path[:])
            if pos >= len(nums):
                return
            
            for i in range(pos, len(nums)):
                if i>pos and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(nums, i+2)
                path.pop()

        dfs(nums, 0)
        return ans

# @lc code=end

