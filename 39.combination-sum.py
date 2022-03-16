#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        candidates.sort()

        def dfs(pos: int, remain: int):
            if remain == 0:
                ans.append(list(path))
                return
            
            for i in range(pos, len(candidates)):
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                dfs(i, remain-candidates[i])
                path.pop()
                    
        dfs(0, target)
        return ans


# @lc code=end

