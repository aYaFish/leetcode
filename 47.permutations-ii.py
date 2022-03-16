#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path, ans = [], []
        counter = Counter(nums)

        def dfs():
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for n in counter:
                if counter[n] == 0:
                    continue
                path.append(n)
                counter[n] -= 1

                dfs()

                path.pop()
                counter[n] += 1

        dfs()
        return ans


# @lc code=end

