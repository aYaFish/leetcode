#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ans = []
        for letter in s:
            if ans and letter == ans[-1][0]:
                if ans[-1][1] == k-1:
                    ans.pop()
                else:
                    ans[-1][1] += 1
            else:
                ans.append([letter, 1])
        return "".join(t[0]*t[1] for t in ans)
        

# @lc code=end

