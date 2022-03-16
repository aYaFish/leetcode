#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        elements = path.split('/')
        ans = []
        for e in elements:
            if e == '.' or not e:
                continue
            elif e == '..':
                if ans:
                    ans.pop()
            else:
                ans.append(e)
        
        return '/' + '/'.join(ans)

        
# @lc code=end

