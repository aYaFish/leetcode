#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, path = [], []

        def dfs(pos: int, r: int):
            if r == 0:
                ans.append(list(path))
                return
            for i in range(pos, n+1):
                path.append(i)
                dfs(i+1, r-1)
                path.pop()

        dfs(1, k)
        return ans
            
# @lc code=end

