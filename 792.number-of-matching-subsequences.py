#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#

# @lc code=start
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        headers = [[] for _ in range(26)]

        # store iter in headers where first letter of word is the key
        for w in words:
            it = iter(w)
            headers[ord(next(it)) - ord("a")].append(it)
        
        count = 0

        # for each letter in s, pop left-over starts with letter,
        # update header with next letter of 
        # iter(word) stored
        for l in s:
            i = ord(l) - ord("a")
            old = headers[i]
            headers[i] = []

            # need to operate on old in case next letter is same as l
            while old: 
                it = old.pop()
                c = next(it, None)
                if c:
                    headers[ord(c) - ord("a")].append(it)
                else:
                    count += 1
        
        return count


    #def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    #    letters = defaultdict(list)
    #    for i, c in enumerate(s):
    #        letters[c].append(i)
    #    
    #    def process(word: str) -> bool:
    #        i = -1
    #        for l in word:
    #            p = bisect_right(letters[l], i)
    #            if p == len(letters[l]):
    #                return False
    #            i = letters[l][p]
    #        return True
    #    
    #    count = 0
    #    for w in words:
    #        if process(w):
    #            count += 1
    #    
    #    return count


# @lc code=end

