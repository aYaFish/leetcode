#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans, path = [], []

        def dfs(pos: int, remain: int) -> None:
            if remain == 0:
                ans.append(list(path))
                return
            
            for i in range(pos, len(candidates)):
                if candidates[i] > remain:
                    break
                if i > pos and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1, remain - candidates[i])
                path.pop()
        
        dfs(0, target)
        return ans
        
# @lc code=end

