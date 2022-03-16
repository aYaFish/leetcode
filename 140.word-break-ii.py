#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
Trie = lambda: defaultdict(Trie)
END = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        trie = Trie()

        for word in wordDict:
            curr = trie
            for letter in word:
                curr = curr[letter]
            curr[END] = True
        
        ret = [None] * (N+1)
        def backtracking(pos: int) -> bool:
            nonlocal ret
            if pos == N:
                ret[N] = []
                return True
            
            if ret[pos] is not None:
                return ret[pos]
            
            curr = trie
            tmp = ""
            for i in range(pos, N):
                if s[i] not in curr:
                    break
                tmp += s[i]
                curr = curr[s[i]]
                if curr[END] and backtracking(i+1):
                    ret[pos] = ret[pos] if ret[pos] else []
                    if ret[i+1]:
                        for r in ret[i+1]:
                            ret[pos].append(f"{tmp} {r}")
                    else:
                        ret[pos].append(tmp)

            if ret[pos] is None:
                ret[pos] = []
                return False
            return True
        
        backtracking(0)
        return ret[0]
        
# @lc code=end

