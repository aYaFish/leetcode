#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans, path = [], []

        def dfs(pos: int, r: int, t: int) -> None:
            if r == 0 and t == 0:
                ans.append(list(path))
                return
            if r == 0 or t == 0:
                return
            
            for i in range(pos, 10):
                if i > t:
                    break
                path.append(i)
                dfs(i+1, r-1, t-i)
                path.pop()
        
        dfs(1, k, n)
        return ans


# @lc code=end

