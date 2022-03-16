#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
Trie = lambda: defaultdict(Trie)
END = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        trie = Trie()

        for word in wordDict:
            curr = trie
            for letter in word:
                curr = curr[letter]
            curr[END] = True
        
        ret = [None] * N
        def backtracking(pos: int) -> bool:
            nonlocal ret
            if pos == N:
                return True
            
            if ret[pos] is not None:
                return ret[pos]
            
            curr = trie
            for i in range(pos, N):
                if s[i] not in curr:
                    break
                curr = curr[s[i]]
                if curr[END] and backtracking(i + 1):
                    ret[pos] = True
                    return True

            ret[pos] = False
            return False
        
        backtracking(0)
        return ret[0] == True


# @lc code=end

