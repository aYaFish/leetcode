#
# @lc app=leetcode id=254 lang=python3
#
# [254] Factor Combinations
#

# @lc code=start
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        path = []
        ans = []
        def dfs(quo, div):
            while div * div <= quo:
                if quo % div == 0:
                    path.append(div)
                    ans.append(path+[quo//div])

                    dfs(quo//div, div)
                    path.pop()
                div += 1
        dfs(n, 2)
        return ans
                

# @lc code=end

