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
        
        @cache
        def backtracking(pos: int) -> bool:
            if pos == N:
                return True
            
            curr = trie
            for i in range(pos, N):
                if s[i] not in curr:
                    break
                curr = curr[s[i]]
                if curr[END] and backtracking(i + 1):
                    return True

            return False
        
        return backtracking(0)


# @lc code=end

