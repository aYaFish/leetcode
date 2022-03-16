#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for letter in s:
            if ans and letter == ans[-1]:
                ans.pop()
            else:
                ans.append(letter)

        return "".join(ans)
# @lc code=end

