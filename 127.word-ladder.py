#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from typing import Iterable


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def neighbors(word: str) -> Iterable:
            for i in range(len(word)):
                for j in range(26):
                    yield word[:i] + chr(j + ord('a')) + word[i + 1:]

        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])
        wordSet.discard(beginWord)
        while queue:
            curr, length = queue.popleft()
            if curr == endWord:
                return length
            for word in neighbors(curr):
                if word in wordSet:
                    queue.append((word, length + 1))
                    wordSet.remove(word)
        
        return 0
        
# @lc code=end

